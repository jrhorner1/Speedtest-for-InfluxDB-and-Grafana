import yaml
import os
import sys


class ConfigManager():

    def __init__(self, config):
        print('Loading Configuration File {}'.format(config))
        self.servers = []
        config_file = os.path.join(os.getcwd(), config)
        if os.path.isfile(config_file):
            #self.config = configparser.ConfigParser()
            #self.config.read(config_file)
            with open(config_file) as file:
                self.config = yaml.load(file, Loader=yaml.FullLoader)
        else:
            print('ERROR: Unable To Load Config File: {}'.format(config_file))
            sys.exit(1)

        self._load_config_values()
        print('Configuration Successfully Loaded')

    def _load_config_values(self):

        # InfluxDB
        self.influx_address = self.config['influxdb']['address']
        self.influx_port = self.config['influxdb']['port']
        self.influx_database = self.config['influxdb']['database']
        self.influx_user = self.config['influxdb']['username']
        self.influx_password = self.config['influxdb']['password']
        self.influx_ssl = self.config['influxdb']['ssl']['enabled']
        self.influx_verify_ssl = self.config['influxdb']['ssl']['verify']

        # Logging
        self.logging_level = self.config['logging']['level']
        self.logging_level = self.logging_level.upper()

        # Speedtest
        self.delay = self.config['speedtest']['interval']
        test_server = self.config['speedtest']['server']
        if test_server:
            self.servers = test_server.split(',')
