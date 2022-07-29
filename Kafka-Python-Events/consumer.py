from kafka import KafkaConsumer

consumer = KafkaConsumer('order_details', bootstrap_servers='localhost:9092')

print("Listening")
while True:
    for message in consumer:
        print("Here is a message..")
        print (message)