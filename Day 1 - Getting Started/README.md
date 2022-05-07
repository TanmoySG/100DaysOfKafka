# Apache Kafka 

## Running Kafka in Docker Container

The `docker-compose.yml` file in the parent directory contains all the required configurations to run Kafka-Broker on Docker, and since the Broker depends on the Zookeeper, the docker-compose file also has the configs for running Zookeeper. Running the docker-compose spins up the Broker and Zookeeper.

```
docker-compose up -d
```

## Kafka Topics 

Kafka topics are the categories used to organize messages. Each topic has a name that is unique across the entire Kafka cluster. Messages are sent to and read from specific topics. In other words, producers write data to topics, and consumers read data from topics.

### Creating a Topic

The Kafka-Broker container has all the kafka console tools required to run operations - create topic, produce message and consume messages, among others.

```
docker exec broker \
kafka-topics --bootstrap-server broker:9092 \
             --create \
             --topic quickstart
```

### Write Messages to Topic

To Produce messages to the broker, we use `kafka-console-producer` CLI Tool

```
docker exec --interactive --tty broker \
kafka-console-producer --bootstrap-server broker:9092 \
                       --topic quickstart
```

This brings up a console-prompt. On the Console, you can write the messages and they'll be produced to the broker. Close the prompt using `Ctrl+D`

### Read messages from the topic

To read messages from broker, use `kafka-console-consumer` tool. Running the following commands shows the Messages written to the Kafka-Topic.

```
docker exec --interactive --tty broker \
kafka-console-consumer --bootstrap-server broker:9092 \
                       --topic quickstart \
                       --from-beginning
```

### Producer-Consumer in Action

To view the Producer-Consumer in Action, Run the `kafka-console-producer` and `kafka-console-consumer` in two separate terminals parallely. Now that both are running, on the Producer Console, Write the messages. You'll see that the messages being written to the broker are being displayed on the consumer console, simultanously.

## Shutdown the Broker

To shut the Broker down use
```
docker-compose down
```