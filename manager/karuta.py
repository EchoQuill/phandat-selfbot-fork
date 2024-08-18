import json
import inquirer

class KarutaManager:
	def __init__(self):
		self.mode = ['Yes', 'No']
		self.file = "configs/karuta.json"

		with open("assets/template.json") as file:
			self.template = json.load(file)['karuta']

		self.features = [
			"Select all",
			"OCR Space (Required)",
			"Drop card",
			"Filter (Print)",
			"Blacklist",
			"Vote top.gg (Require chorme)",
			"Discord command",
			"Discord webhook",
			"Log file",
			"Log image",
			"Music notification",
			"Retry errors"
		]

	def homepage(self):
		with open(self.file) as file:
			config = json.load(file)
		choices = ['Back', 'Add accounts', 'Remove accounts']
		for account in config:
			choices.append(account)
		select = inquirer.list_input("Move ↑↓ and ENTER to select", choices = choices)
		if select == "Back":
			return
		elif select == "Add accounts":
			self.add_accounts()
		elif select == "Remove accounts":
			self.remove_accounts()
		else:
			self.change_accounts(select)
		self.homepage()

	def add_accounts(self):
		with open(self.file) as file:
			config = json.load(file)
		while True:
				token = input("[!] Enter a discord token: ")
				if not token == "" and not " " in token:
					break
				print("[-] Token mustn't be empty or have spaces")
		account = {token: self.template}
		config.update(account)
		with open(self.file, "w") as file:
			json.dump(config, file, indent = 4)
		print("[+] Added a new account")
		self.change_accounts(token, True)

	def remove_accounts(self):
		with open(self.file) as file:
			config = json.load(file)
		choices = []
		for account in config:
			choices.append(account)
		select = inquirer.checkbox("Move ↑↓ and SPACE to choose, then ENTER to select", choices = choices)
		amount = 0
		for account in select:
			amount += 1
			del config[account]
		with open(self.file, 'w') as file:
			json.dump(config, file, indent = 4)
		if amount > 0:
			print(f"[-] Removed {amount} {"account" if amount == 1 else "accounts"}")

	def change_accounts(self, token, select_all = False):
		with open(self.file) as file:
			config = json.load(file)

		if not select_all:
			select = inquirer.checkbox("Move ↑↓ and SPACE to choose, then ENTER to select", choices = self.features)
			if "Select all" in select:
				select_all = True

		if select_all or "OCR Space (Required)" in select:
			self.ocr_space(token, config)

		if select_all or "Drop card" in select:
			self.drop_card(token, config)

		if select_all or "Filter (Print)" in select:
			self.filter(token, config)

		if select_all or "Blacklist" in select:
			self.blacklist(token, config)

		if select_all or "Vote top.gg (Require chorme)" in select:
			self.topgg(token, config)

		if select_all or "Discord command" in select:
			self.command(token, config)

		if select_all or "Discord webhook" in select:
			self.webhook(token, config)

		if select_all or "Log file" in select:
			self.log_file(token, config)

		if select_all or "Log image" in select:
			self.log_image(token, config)

		if select_all or "Music notification" in select:
			self.music_notification(token, config)

		if select_all or "Retry errors" in select:
			self.error_retry_times(token, config)

		with open(self.file, 'w') as file:
			json.dump(config, file, indent = 4)
		print("[+] Saved!")

	def ocr_space(self, token, config):
		print("[!] Get OCR Space API in https://ocr.space/ocrapi/freekey")
		while True:
			try:
				amount = int(input(f"[!] Enter the amount of OCR Space API for image analysis (E.g: 1) (Recent: {config[token]['ocr_space']}): ")) + 1
				break
			except ValueError:
				print("[-] Must be a number")
		ocr_space = []
		for num in range(1, amount):
			x = input(f"[!] Enter the OCR Space API {num}: ")
			ocr_space.append(x)
		config[token]['ocr_space'] = ocr_space

	def drop_card(self, token, config):
		print(f"[!] Drop card (Recent: {config[token]['drop_card']['mode']})")
		select = inquirer.list_input("Move ↑↓ and ENTER to select", choices = self.mode)
		config[token]['drop_card']['mode'] = select == "Yes"
		if config[token]['drop_card']['mode']:
			while True:
				try:
					amount = int(input(f"[!] Enter the amount of dropping card channel id (E.g: 3) (Recent: {config[token]['drop_card']['channel_id']}): ")) + 1
					break
				except ValueError:
					print("[-] Must be a number")
			dropping_card_channel_id = []
			for num in range(1, amount):
				while True:
					try:
						x = int(input(f"[!] Enter the quest channel id {num}: "))
						break
					except ValueError:
						print("[-] Must be a number")
				dropping_card_channel_id.append(x)
			config[token]['drop_card']['channel_id'] = dropping_card_channel_id

	def filter(self, token, config):
		while True:
			try:
				prints = int(input(f"[!] Enter the lowest print number of card to grab (E.g: 5000) (Recent: {config[token]['filter']['print']}): "))
				break
			except ValueError:
				print("[-] Must be a number")
		config[token]['filter']['print'] = prints

	def blacklist(self, token, config):
		print(f"[!] What do you wanna block")
		print(f"Recent: (User id: {config[token]['blacklist']['user_id']}/Channel id: {config[token]['blacklist']['channel_id']})")
		select = inquirer.checkbox("Move ↑↓ and SPACE to choose, then ENTER to select", choices = ['User id', 'Channel id', 'Guild id'])
		config[token]['blacklist']['user_id'] = []
		config[token]['blacklist']['channel_id'] = []
		config[token]['blacklist']['guild_id'] = []

		if "User id" in select:
			while True:
				try:
					amount = int(input(f"[!] Enter the amount of user id to block (E.g: 3) (Recent: {config[token]['blacklist']['user_id']}): ")) + 1
					break
				except ValueError:
					print("[-] Must be a number")
			user_id = []
			for num in range(1, amount):
				while True:
					try:
						x = int(input(f"[!] Enter the blocked user id {num}: "))
						break
					except ValueError:
						print("[-] Must be a number")
				user_id.append(x)
			config[token]['blacklist']['user_id'] = user_id

		if "Channel id" in select:
			while True:
				try:
					amount = int(input(f"[!] Enter the amount of channel id to block (E.g: 3) (Recent: {config[token]['blacklist']['channel_id']}): ")) + 1
					break
				except ValueError:
					print("[-] Must be a number")
			channel_id = []
			for num in range(1, amount):
				while True:
					try:
						x = int(input(f"[!] Enter the blocked channel id {num}: "))
						break
					except ValueError:
						print("[-] Must be a number")
				channel_id.append(x)
			config[token]['blacklist']['channel_id'] = channel_id

		if "Guild id" in select:
			while True:
				try:
					amount = int(input(f"[!] Enter the amount of guild id to block (E.g: 3) (Recent: {config[token]['blacklist']['guild_id']}): ")) + 1
					break
				except ValueError:
					print("[-] Must be a number")
			guild_id = []
			for num in range(1, amount):
				while True:
					try:
						x = int(input(f"[!] Enter the blocked guild id {num}: "))
						break
					except ValueError:
						print("[-] Must be a number")
				guild_id.append(x)
			config[token]['blacklist']['guild_id'] = guild_id

	def topgg(self, token, config):
		print(f"[!] Vote top.gg (Require chorme) (Recent: {config[token]['topgg']})")
		select = inquirer.list_input("Move ↑↓ and ENTER to select", choices = self.mode)
		config[token]['topgg'] = select == "Yes"

	def command(self, token, config):
		print("[!] Discord command")
		select = inquirer.list_input("Move ↑↓ and ENTER to select", choices = self.mode)
		config[token]['command']['mode'] = select == "Yes"
		if config[token]['command']['mode']:
			while True:
				try:
					amount = int(input("[!] Enter the amount of owner id (E.g: 3): ")) + 1
					break
				except ValueError:
					print("[-] Must be a number")
			owner_id = []
			for num in range(1, amount):
				while True:
					try:
						x = int(input(f"[!] Enter the owner id {num}: "))
						break
					except ValueError:
						print("[-] Must be a number")
				owner_id.append(x)
			config[token]['command']['owner_id'] = owner_id

	def webhook(self, token, config):
		print(f"[!] Discord webhook (Recent: {config[token]['webhook']['mode']})")
		select = inquirer.list_input("Move ↑↓ and ENTER to select", choices = self.mode)
		config[token]['webhook']['mode'] = select == "Yes"
		if config[token]['webhook']['mode']:
			while True:
				try:
					amount = int(input(f"[!] Enter the amount of mentioner id (E.g: 3) (Recent: {config[token]['webhook']['mentioner_id']}): ")) + 1
					break
				except ValueError:
					print("[-] Must be a number")
			mentioner_id = []
			for num in range(1, amount):
				while True:
					try:
						x = int(input(f"[!] Enter the mentioner id {num}: "))
						break
					except ValueError:
						print("[-] Must be a number")
				mentioner_id.append(x)
			config[token]['webhook']['mentioner_id'] = mentioner_id
			config[token]['webhook']['url'] = input(f"[!] Enter the webhook url (E.g: discord.com/api/webhooks/123/abc) (Recent: {config[token]['webhook']['url']}): ")

	def log_file(self, token, config):
		print(f"[!] Log file (Recent: {config[token]['log_file']})")
		select = inquirer.list_input("Move ↑↓ and ENTER to select", choices = self.mode)
		config[token]['log_file'] = select == "Yes"

	def log_image(self, token, config):
		print(f"[!] Log image (Recent: {config[token]['log_image']})")
		select = inquirer.list_input("Move ↑↓ and ENTER to select", choices = self.mode)
		config[token]['log_image'] = select == "Yes"

	def music_notification(self, token, config):
		print(f"[!] Music notification (Recent: {config[token]['music_notification']})")
		select = inquirer.list_input("Move ↑↓ and ENTER to select", choices = self.mode)
		config[token]['music_notification'] = select == "Yes"

	def error_retry_times(self, token, config):
		while True:
			try:
				times = int(input(f"[!] Enter error retry times (E.g: 10) (Recent: {config[token]['error_retry_times']}): "))
				break
			except ValueError:
				print("[-] Must be a number")
		config[token]['error_retry_times'] = times