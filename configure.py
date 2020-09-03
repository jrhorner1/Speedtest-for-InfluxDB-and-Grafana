import os 

# Configure the application from environement variables
with open(r"/src/config.ini", "w") as configFile:
	configFile.write("[GENERAL]\n")
	configFile.write("Delay = " + os.environ.get('TEST_DELAY') + "\n\n")
	configFile.write("[INFLUXDB]\n")
	configFile.write("Address = " + os.environ.get('INFLUX_ADDR') + "\n")
	configFile.write("Port =  " + os.environ.get('INFLUX_PORT') + "\n")
	configFile.write("Database =  " + os.environ.get('INFLUX_DB') + "\n")
	configFile.write("Username =  " + os.environ.get('INFLUX_USER') + "\n")
	configFile.write("Password =  " + os.environ.get('INFLUX_PASS') + "\n")
	configFile.write("Verify_SSL =  " + os.environ.get('INFLUX_VERIFYSSL') + "\n\n")
	configFile.write("[SPEEDTEST]\n")
	configFile.write("Server =  " + os.environ.get('TEST_SERVER') + "\n\n")
	configFile.write("[LOGGING]\n")
	configFile.write("Level =  " + os.environ.get('LOG_LEVEL') + "\n")

with open(r"/src/config.ini", "r") as configFile:
	print(configFile.read())