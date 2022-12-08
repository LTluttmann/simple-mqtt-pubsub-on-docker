FROM python:latest

RUN apt-get update
RUN apt-get install -y mosquitto
RUN apt-get install -y mosquitto-clients

RUN pip install jupyter
RUN pip install paho-mqtt

#WORKDIR /home/
COPY app.py .
CMD python app.py

#EXPOSE ${JUPYTER_PORT}

#CMD jupyter notebook --port ${JUPYTER_PORT} --ip 0.0.0.0 --no-browser --allow-root