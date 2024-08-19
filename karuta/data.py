import time
import json
import random

class Data:
	def __init__(self, token):
		self.config = Config(token)

		self.bot = Bot()
		self.stat = Stat()
		self.emoji =  Emoji()
		self.discord = Discord()
		self.selfbot = Selfbot()
		self.cooldown = Cooldown()
		self.available = Available()

class Config:
	def __init__(self, token):
		self.file = "configs/karuta.json"
		with open(self.file) as file:
			data = json.load(file)
			self.token = token
			self.ocr_space = data[token]['ocr_space']
			self.drop_card = data[token]['drop_card']
			self.filter = data[token]['filter']
			self.blacklist = data[token]['blacklist']
			self.topgg = data[token]['topgg']
			self.command = data[token]['command']
			self.webhook = data[token]['webhook']
			self.log_file = data[token]['log_file']
			self.log_image = data[token]['log_image']
			self.music_notification = data[token]['music_notification']
			self.error_retry_times = data[token]['error_retry_times']

class Bot:
	def __init__(self):
		self.id = 646937666251915264

class Stat:
	def __init__(self):
		self.drop_card = 0
		self.grab_card = 0

class Emoji:
	def __init__(self):
		self.arrow = "<a:Arrow:1065047400714088479>"
		self.number = ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]

class Discord:
	def __init__(self):
		self.prefix = "k!"
		self.mention = ""

class Selfbot:
	def __init__(self):
		self.on_ready = True
		self.turn_on_time = time.time()

class Cooldown:
	def __init__(self):
		self.drop_card = 0
		self.grab_card = 0

class Available:
	def __init__(self):
		self.selfbot = True
		self.checking = False