import discord

from karuta.data import Data
from public.log import Log
from public.topgg import Topgg
from karuta.tasks import Tasks
from karuta.modules import Modules
from karuta.commands import Commands
from public.webhooks import Webhooks
from public.notification import Notification

class KarutaSelfbot(discord.Client):
	def __init__(self, token, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.data = Data(token)
		self.log = Log(self)
		self.topgg = Topgg(self)
		self.tasks = Tasks(self)
		self.modules = Modules(self)
		self.commands = Commands(self)
		self.webhooks = Webhooks(self)
		self.notification = Notification(self)
	
	async def on_ready(self):
		if self.data.selfbot.on_ready:
			self.data.selfbot.on_ready = False
			self.data.bot = self.get_user(self.data.bot.id)
			self.logger = await self.log.create("karuta")
			await self.modules.startup()
			await self.modules.intro()
			await self.tasks.start()

	async def on_message(self, message):
		await self.modules.check_image(message)
		await self.modules.get_cooldown(message)
		if self.data.config.command['mode']:
			await self.modules.command(message)