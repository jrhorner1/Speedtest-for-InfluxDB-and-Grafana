import os 

# Configure the application from environement variables
with open(r"/src/config.yml", "w") as configFile:
	configFile.write("influxdb:\n")
	configFile.write("  address: " + os.environ.get('INFLUX_ADDR') + "\n")
	configFile.write("  port: " + os.environ.get('INFLUX_PORT') + "\n")
	configFile.write("  database: " + os.environ.get('INFLUX_DB') + "\n")
	configFile.write("  username: " + os.environ.get('INFLUX_USER') + "\n")
	configFile.write("  password: " + os.environ.get('INFLUX_PASS') + "\n")
	configFile.write("  ssl:\n")
	configFile.write("    enabled: " + os.environ.get('INFLUX_SSL_ENABLED') + "\n")
	configFile.write("    verify: " + os.environ.get('INFLUX_SSL_VERIFY') + "\n\n")
	configFile.write("speedtest:\n")
	configFile.write("  server:  " + os.environ.get('TEST_SERVER') + "\n")
	configFile.write("  interval: " + os.environ.get('TEST_DELAY') + "\n\n")
	configFile.write("logging:\n")
	configFile.write("  level:  " + os.environ.get('LOG_LEVEL') + "\n")

with open(r"/src/config.yml", "r") as configFile:
	print(configFile.read())