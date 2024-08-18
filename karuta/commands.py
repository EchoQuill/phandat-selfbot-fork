import discord
import asyncio
import json

class Commands:
	def __init__(self, client):
		self.client = client

	async def help(self):
		menu = """
**`start`
`pause`

`help`
`stat`
`setting`

`say` + `-text`**
"""
		self.client.logger.info(f"Sent command menu via webhook")
		await self.client.webhooks.send(
			title = f"📋 COMMAND MENU 📋",
			description = menu,
			color = discord.Colour.random()
		)

	async def start_selfbot(self):
		self.client.data.available.selfbot = True
		self.client.logger.info(f"Start selfbot")
		await self.client.webhooks.send(
			title = f"🌤️ START SELFBOT 🌤️",
			color = discord.Colour.random()
		)

	async def pause_selfbot(self):
		self.client.data.available.selfbot = False
		self.client.logger.info(f"Pause selfbot")
		await self.client.webhooks.send(
			title = f"🌑 PAUSE SELFBOT 🌑",
			color = discord.Colour.random()
		)

	async def stat_selfbot(self):
		stat = f"""
**Worked <t:{int(self.client.data.selfbot.turn_on_time)}:R> with:
{self.client.data.emoji.arrow}Dropped __{self.client.data.stat.drop_card}__ cards
{self.client.data.emoji.arrow}Grabbed __{self.client.data.stat.grab_card}__ cards**
"""
		self.client.logger.info(f"Sent stat via webhook")
		await self.client.webhooks.send(
			title = f"📊 STAT 📊",
			description = stat,
			color = discord.Colour.random()
		)

	async def show_setting(self):
		await self.client.webhooks.send(
			title = f"🔥 CONFIRM `YES` IN 10S 🔥",
			description = "**Send setting via webhook including __token__, __TwoCaptcha API__, __webhook url__, ...**",
			color = discord.Colour.random()
		)
		try:
			await self.client.wait_for("message", check = lambda message: message.content.lower() in ['yes', 'y'] and message.author.id in self.client.data.config.command['owner_id'], timeout = 10)
		except asyncio.TimeoutError:
			pass
		else:
			self.client.logger.info(f"Sent setting via webhook")
			with open(self.client.data.config.file) as file:
				config = json.load(file)
			await self.client.webhooks.send(
				title = f"💾 SETTING 💾",
				description = config[self.client.data.config.token],
				color = discord.Colour.random()
			)

	async def say_text(self, message):
		text = message.content.split("-")[1]
		await message.channel.send(text)
		self.client.logger.info(f"Sent {text}")