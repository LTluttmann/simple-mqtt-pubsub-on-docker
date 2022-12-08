FROM python:latest

RUN apt-get update
RUN apt-get install -y mosquitto
RUN apt-get install -y mosquitto-clients

CMD mosquitto_sub -h ${BROKERNAME} -t ${TOPIC}
