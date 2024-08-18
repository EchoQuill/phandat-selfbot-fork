import json
import inquirer

from manager.owo import OwOManager
from manager.karuta import KarutaManager

class Key:
	def __init__(self):
		self.file = "configs/key.json"

	def homepage(self):
		with open(self.file) as file:
			config = json.load(file)
		select = inquirer.list_input("Move ↑↓ and ENTER to select", choices = ['Back', 'Payment', 'Trial'])
		if select == "Back":
			return
		if select == "Payment":
			config['payment'] = input(f"Enter the payment key (Recent: {config['payment']}): ")
		if select == "Trial":
			config['trial'] = input(f"Enter the trial key (Recent: {config['trial']}): ")
		with open(self.file, "w") as file:
			json.dump(config, file, indent = 4)
		print("[+] Saved!")
		self.homepage()

class Mode:
	def __init__(self):
		self.mode = ['Yes', 'No']
		self.file = "configs/mode.json"

	def homepage(self):
		with open(self.file) as file:
			config = json.load(file)
		select = inquirer.list_input("Move ↑↓ and ENTER to select", choices = ['Back', 'OwO Selfbot', 'Karuta Selfbot'])
		if select == "Back":
			return
		if select == "OwO Selfbot":
			self.owo_selfbot(config)
		if select == "Karuta Selfbot":
			self.karuta_selfbot(config)
		with open(self.file, "w") as file:
			json.dump(config, file, indent = 4)
		print("[+] Saved!")
		self.homepage()

	def owo_selfbot(self, config):
		print(f"[!] OwO Selfbot (Recent: {config['owo']})")
		select = inquirer.list_input("Move ↑↓ and ENTER to select", choices = self.mode)
		config['owo'] = select == "Yes"

	def karuta_selfbot(self, config):
		print(f"[!] Karuta Selfbot (Recent: {config['karuta']})")
		select = inquirer.list_input("Move ↑↓ and ENTER to select", choices = self.mode)
		config['karuta'] = select == "Yes"

def start():
	select = inquirer.list_input("Move ↑↓ and ENTER to select", choices = ['Key', 'Mode', 'OwO Manager', 'Karuta Manager'])
	if select == "Key":
		key = Key()
		key.homepage()
	if select == "Mode":
		mode = Mode()
		mode.homepage()
	if select == "OwO Manager":
		owo_manager = OwOManager()
		owo_manager.homepage()
	if select == "Karuta Manager":
		karuta_manager = KarutaManager()
		karuta_manager.homepage()
	start()

if __name__ == "__main__":
	start()