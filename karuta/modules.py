import discord
import cv2
import re
import io
import json
import numpy
import time
import random
import requests
import asyncio

from PIL import Image

class Modules:
	def __init__(self, client):
		self.client = client

	async def startup(self):
		mentioner_id = set(self.client.data.config.webhook['mentioner_id'])
		mentioner_id.add(self.client.user.id)
		self.client.data.discord.mention = ''.join(f"<@{i}>" for i in mentioner_id)

	async def intro(self):
		webhook = ""
		if self.client.data.config.command['mode']:
			webhook = f"**{self.client.data.emoji.arrow}Send `help` or `<@{self.client.user.id}> help`**"
		await self.client.webhooks.send(
			title = f"🚀 STARTED <t:{int(self.client.data.selfbot.turn_on_time)}:R> 🚀",
			description = webhook,
			color = discord.Colour.random()
		)

	async def get_cooldown(self, message):
		if message.author.id != self.client.data.bot.id:
			return

		matches = re.findall(f"<@{self.client.user.id}>, you must wait `(.*?)` before", message.content)
		if not matches:
			return

		if "seconds" in matches[0]:
			cooldown = int(re.findall(r'\d+', matches[0])[0])
		elif "minutes" in matches[0]:
			cooldown = int(re.findall(r'\d+', matches[0])[0]) * 60

		if "dropping more" in message.content:
			self.client.logger.info(f"Drop more cards after {matches[0]}")
			self.client.data.cooldown.drop_card = cooldown + time.time()
		if "grabbing another" in message.content:
			self.client.logger.info(f"Grab another card after {matches[0]}")
			self.client.data.cooldown.grab_card = cooldown + time.time()

	async def drop_card(self):
		if not self.client.data.available.selfbot:
			return
		if self.client.data.available.checking:
			return
		if self.client.data.cooldown.drop_card - time.time() > 0:
			return
		if self.client.data.cooldown.grab_card - time.time() > 0:
			return

		channel = self.client.get_channel(int(random.choice(self.client.data.config.drop_card['channel_id'])))
		await channel.send(f"{self.client.data.discord.prefix}d")
		self.client.logger.info(f"Dropped in {channel} ({channel.id})")
		self.client.data.stat.drop_card += 1

	async def grab_card(self, message, position, runtime, retry_times, image):
		if retry_times >= int(self.client.data.config.error_retry_times):
			self.client.logger.info(f"Stop checking grabbing card after {self.client.data.config.error_retry_times} retry times")
			return

		number = position + 1
		if message.components:
			async for m in message.channel.history(limit = self.client.data.config.error_retry_times):
				if m.id == message.id and m.components and not m.components[0].children[0].disabled:
					button = m.components[0].children[position]
					await button.click()
					clicker = "button"
					break
			else:
				retry_times += 1
				await self.grab_card(message, position, runtime, retry_times, image)
				return
		else:
			try:
				emoji = self.client.data.emoji.number[position] if 0 <= position < len(self.client.data.emoji.number) else position
				await message.add_reaction(emoji)
				clicker = "emoji"
			except discord.errors.Forbidden:
				retry_times += 1
				await self.grab_card(message, position, runtime, retry_times, image)
				return

		self.client.logger.info(f"Click {clicker} {number} ({(time.time() - runtime):.5f} seconds)")

		try:
			grabbing_message = await self.client.wait_for("message", check = lambda m: m.author.id == self.client.data.bot.id and m.channel.id == message.channel.id and (f"<@{self.client.user.id}> took the" in m.content or "fought off" in m.content), timeout = 5)
			if f"<@{self.client.user.id}> took the" in grabbing_message.content or f"<@{self.client.user.id}> fought off" in grabbing_message.content:
				self.client.logger.info(f"Grabbed card number {number}")
				self.client.data.cooldown.grab_card = 600 + time.time()
			else:
				self.client.logger.info(f"Someone fought off and took card number {number}")
				self.client.data.cooldown.grab_card = 60 + time.time()
		except asyncio.TimeoutError:
			self.client.logger.error(f"Couldn't get grabbing message")

		if self.client.data.config.log_image:
			file = f"logs/karuta/image/{message.id}.png"
			cv2.imwrite(file, image)
			self.client.logger.info(f"Added {file}")

		await self.client.webhooks.send(
			title = f"🎴 GRAB CARD {number} 🎴",
			description = f"{self.client.data.emoji.arrow}{message.jump_url}",
			color = discord.Colour.random(),
			thumnail = message.attachments[0]
		)
		self.client.data.stat.grab_card += 1

	async def check_image(self, message):
		try:
			if not self.client.data.available.selfbot:
				return
			if self.client.data.available.checking:
				return
			if self.client.data.cooldown.grab_card - time.time() > 0:
				return
			if message.author.id != self.client.data.bot.id:
				return

			amount = re.findall(r"dropping ([0-9]+) cards", message.content)
			amount = int(amount[0]) if amount else None
			if not amount:
				return
			
			self.client.logger.info(f"Detect a karuta image in {message.channel} ({message.id})")

			if any(f"<@{user_id}>" in message.content for user_id in self.client.data.config.blacklist['user_id']):
				self.client.logger.info(f"Message is on user id blacklist ({message.author.id})")
				return
			if message.channel.id in self.client.data.config.blacklist['channel_id']:
				self.client.logger.info(f"Message is on channel id blacklist ({message.channel.id})")
				return
			if message.guild.id in self.client.data.config.blacklist['guild_id']:
				self.client.logger.info(f"Message is on guild id blacklist ({message.guild.id})")
				return

			runtime = time.time()
			self.client.data.available.checking = True

			with Image.open(io.BytesIO(requests.get(message.attachments[0].url).content)) as image:
				image = numpy.array(image)

			result = list(filter(bool, await self.ocr_image(image[365:390], 5)))
			if not result:
				self.client.logger.error(f"Error image to text (OCR)")
				return
			if len(result) != amount:
				self.client.logger.warning(f"Incorrect image to text (OCR)")
				return

			prints = []
			for i in range(0, amount):
				answer = re.findall(r'\d+', result[i])[0]
				prints.append(int(answer))

			lowest = min(prints)
			if lowest > int(self.client.data.config.filter['print']):
				self.client.logger.info(f"Cards prints has under {self.client.data.config.filter['print']}")
				return
			position = prints.index(lowest)
			await self.grab_card(message, position, runtime, 0, image)
		finally:
			self.client.data.available.checking = False

	async def ocr_image(self, image, scale):
			try:
				# image = cv2.resize(image, None, fx = scale, fy = scale, interpolation=cv2.INTER_LINEAR)
				nothing, image_encode = cv2.imencode('.png', image)
				string_encode = image_encode.tobytes()
				image_byteio = io.BytesIO(string_encode)
				image_byteio.name = 'image.png'
				image = io.BufferedReader(image_byteio)

				api_key = random.choice(self.client.data.config.ocr_space)
				response = requests.post('https://api.ocr.space/parse/image', files = {"image.png": image}, data = {'apikey': api_key, 'OCREngine': 2})
				result = json.loads(response.content.decode())['ParsedResults'][0]['ParsedText']
				result = result.split("\n") #OCREngine 1 (\r\n) - OCREngine (\n)
				return result
			except (KeyError, IndexError):
				return

	def filter_command(self, message):
			command = message.content
			if message.content.startswith(f"<@{self.client.user.id}>"):
				command = message.content.replace(f"<@{self.client.user.id}>", "", 1)
			command = filter(bool, command.split(" "))
			return(list(command))

	async def command(self, message):
		if message.author.id in self.client.data.config.command['owner_id'] or message.author.id == self.client.user.id:
			command = self.filter_command(message)
			if not command:
				return

			if command[0].lower() == "start":
				await self.client.commands.start_selfbot()
			if command[0].lower() == "pause":
				await self.client.commands.pause_selfbot()

			if command[0].lower() == "help":
				await self.client.commands.help()
			if command[0].lower() == "stat":
				await self.client.commands.stat_selfbot()
			if command[0].lower() == "setting":
				await self.client.commands.show_setting()

			if command[0].lower() == "say" and "-" in message.content and len(command) >= 2:
				await self.client.commands.say_text(message)
