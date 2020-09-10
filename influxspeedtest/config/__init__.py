import os

from influxspeedtest.config.configmanager import ConfigManager

if os.getenv('speedtest_config'):
    config = os.getenv('speedtest_config')
else:
    config = 'config.yml'

config = ConfigManager(config)