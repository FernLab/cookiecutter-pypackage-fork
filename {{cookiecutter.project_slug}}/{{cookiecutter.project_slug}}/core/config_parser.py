from configparser import ConfigParser

CONFIG_FILE = "./core/config.ini"
config = ConfigParser()

if not config.read(CONFIG_FILE):
    raise Exception(
        f"Error reading Configuration File => {CONFIG_FILE} Not Found!.")
else:
    config.read(CONFIG_FILE)
