
import json
import time

from kafka import KafkaProducer

ORDER_KAFKA_TOPIC = "example_topic"
ORDER_LIMIT = 15

producer = KafkaProducer(bootstrap_servers="localhost:9092")

for i in range(ORDER_LIMIT):
    data = {
        "order_id": i,
        "user_id": f"tom_{i}",
        "total_cost": i,
        "items": "burger,sandwich",
    }

    producer.send("example_topic", json.dumps(data).encode("utf-8"))
    print(f"Done Sending..{i}")