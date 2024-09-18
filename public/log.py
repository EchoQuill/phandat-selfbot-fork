import logging, logging.handlers

class CustomFormatter(logging.Formatter):
	template = "%(asctime)s - %(name)s - [%(levelname)s] %(message)s"

	def __init__(self, is_file = False):
		super().__init__(datefmt = "%d %b %Y %H:%M:%S")
		self.is_file = is_file

	def format(self, record):
		log_fmt = self.template
		formatter = logging.Formatter(fmt = log_fmt, datefmt = self.datefmt)
		return formatter.format(record)

class Log:
	def __init__(self, client):
		self.client = client

	async def create(self, name):
		logger = logging.getLogger(f"[{name.upper()}] - {str(self.client.user.name)}")
		logger.setLevel(logging.DEBUG)
		console_handler = logging.StreamHandler()
		console_handler.setFormatter(CustomFormatter())
		logger.addHandler(console_handler)
		if self.client.data.config.log_file:
			file = f"logs/{name}/{str(self.client.user.name)}.txt"
			file_handler = logging.handlers.WatchedFileHandler(file, encoding = "utf-8", mode = "a+")
			file_handler.setFormatter(CustomFormatter())
			logger.addHandler(file_handler)
			logger.info(f"Created {file}")
		return logger