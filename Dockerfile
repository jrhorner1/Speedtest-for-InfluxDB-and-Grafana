FROM python:alpine
MAINTAINER Barry Carey <mcarey66@gmail.com>

ENV INFLUX_ADDR=""
ENV INFLUX_PORT="8086"
ENV INFLUX_DB="speedtests"
ENV INFLUX_USER=""
ENV INFLUX_PASS=""
ENV INFLUX_VERIFYSSL="False"
ENV TEST_DELAY="300"
ENV TEST_SERVER=""
ENV LOG_LEVEL="info"

VOLUME /src/
COPY influxspeedtest.py requirements.txt config.yml configure.py /src/
ADD influxspeedtest /src/influxspeedtest
WORKDIR /src

RUN pip install -r requirements.txt

CMD ["python", "-u", "/src/influxspeedtest.py"]
