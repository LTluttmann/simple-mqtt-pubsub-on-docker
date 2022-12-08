# simple-mqtt-pubsub-on-docker
Repo for learning about Docker, message broker and pub/sub architectures

After the "docker-compose up command", the 

- client will be available under localhost:8888 using the logged token

- rabbitmq management console will be available under localhost:15672 using credentials guest guest

The consumer container will be built when the broker is ready and subscribe to the topic specified in .env file. As soon as the consumer container is ready, the client is built and fires some messages to the queue $TOPIC. These will be logged on the stdout of the host machine