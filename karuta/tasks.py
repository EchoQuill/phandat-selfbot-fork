import asyncio
import random

from discord.ext import tasks

class Tasks:
	def __init__(self, client):
		self.client = client
		self.tasks = [
			self.drop_card,
			self.vote_topgg,
		]

	async def start(self, skip = None):
		self.client.data.available.selfbot = True
		for task in self.tasks:
			if skip:
				if task in skip:
					continue
			try:
				task.start()
				await asyncio.sleep(random.randint(10, 20))
			except RuntimeError:
				pass

	async def stop(self, skip = None):
		self.client.data.available.selfbot = False
		for task in self.tasks:
			if skip:
				if task in skip:
					continue
			task.cancel()

	@tasks.loop(minutes = 1)
	async def drop_card(self):
		if self.client.data.config.drop_card['mode']:
			await self.client.modules.drop_card()

	@tasks.loop(hours = 12)
	async def vote_topgg(self):
		if self.client.data.config.topgg:
			await self.client.topgg.vote()