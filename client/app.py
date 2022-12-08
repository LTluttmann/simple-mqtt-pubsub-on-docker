import os
import time
import paho.mqtt.client as mqtt

HOST = os.getenv("BROKERNAME")
PORT = int(os.getenv("MQTT_PORT"))
TOPIC = os.getenv("TOPIC") 

conn = 1
while not conn == 0:
  client = mqtt.Client()
  try:
    conn = client.connect(HOST, PORT)
  except:
    conn = 1
  print("connection: ", conn)

i = 0
while True:
  time.sleep(5)
  i+=1
  message = str(i)
  if i <=10:
    client.publish(TOPIC, message)
  else:
    break
client.disconnect()
