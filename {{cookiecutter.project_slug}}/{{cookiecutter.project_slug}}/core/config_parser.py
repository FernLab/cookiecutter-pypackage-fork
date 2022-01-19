import os
from configparser import ConfigParser

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
config = ConfigParser()

if not config.read(CONFIG_FILE):
    raise FileNotFoundError("Config.ini file not found!.")
else:
    config.read(CONFIG_FILE)
