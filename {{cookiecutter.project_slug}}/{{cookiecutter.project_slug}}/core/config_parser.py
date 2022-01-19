import os
from configparser import ConfigParser

config = ConfigParser()

try:
    CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
    if not config.read(CONFIG_FILE):
        raise Exception("Empty configuration file!")
    else:
        config.read(CONFIG_FILE)
except Exception as e:
    raise Exception(f"Unable to read config.ini file => {e}!")
