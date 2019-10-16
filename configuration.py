from configparser import SafeConfigParser
from logconfig import logger

import codecs

config = SafeConfigParser()

config.read('config.ini')