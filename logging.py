import logging

# Create a logger instance
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Create a custom log formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a file handler and configure it
file_handler = logging.FileHandler('my_log_file.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Create a console handler and configure it
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Log messages
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
