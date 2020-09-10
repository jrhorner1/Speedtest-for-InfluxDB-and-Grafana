**Speedtest.net Collector For InfluxDB and Grafana**
------------------------------

![Screenshot](https://puu.sh/tmfOA/b5576e88de.png)

This tool is a wrapper for speedtest-cli which allows you to run periodic speedtets and save the results to Influxdb 

## Configuration within config.yml

|Key                     |Default    |Description                                           |
|:-----------------------|:----------|:-----------------------------------------------------|
|influxdb.address        |influxdb   |HTTP address of the influxdb server                   |
|influxdb.port           |8086       |Listening port of the influxdb server                 |
|influxdb.database       |speedtests |Database to write collected stats to                  |
|influxdb.username       |           |User that has access to the database                  |
|influxdb.password       |           |Password for above user                               |
|influxdb.ssl.enabled    |False      |                                                      |
|influxdb.ssl.verify     |False      |                                                      |
|speedtest.server        |           |Comma separated list of servers. Leave blank for auto |
|speedtest.interval      |300        |Delay between runs                                    |
|logging.level           |info       |Valid Options: critical, error, warning, info, debug  |

## Usage

### Build

```bash
docker build . -t speedtest:latest
```

### Docker Compose

The included docker-compose file should be every needed to get going fast. Make sure to build the project first, then run the following:
```bash
docker-compose up
```
Access Grafana at `http://localhost:3000` and login with the default username: `admin` and password: `admin`. You will be prompted to change the password.

### Helm

For deploying to a kubernetes cluster. Create a my-values.yml file and update any values as you see fit.

my-values.yml 
```yaml
image:
  repository: speedtest:latest # Local image that you build earlier
# Application settings:
influxdb:
  address: "influxdb.default" # Influxdb server
  port: "8086"  # Influxdb server port
  database: "speedtests" # Database to write collected stats to
  username: "admin" # User that has access to the database
  password: "admin" # Password for above user
  ssl:
    enabled: "False"
    verify: "False"
speedtest:
  delay: "300"  # Delay between runs
  server: ""  # Comma separated list of servers. Leave blank for auto
logging:  
  level: "info" # Valid Options: critical, error, warning, info, debug
```


```bash
helm install my-app . -f my-values.yml -n my-namespace
```