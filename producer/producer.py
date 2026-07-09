from kafka import KafkaProducer
from faker import Faker
import json 
import random
import time
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

fake = Faker("en_IN")

print("Sending Orders...\n")

while True:

    order = {
        "OrderID": random.randint(100000,999999),
        "CustomerID": random.randint(1,10000),
        "ProductID": random.randint(1,1000),
        "Quantity": random.randint(1,5),
        "Price": random.randint(100,5000),
        "City": fake.city(),
        "OrderTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    producer.send("orders", order)
    producer.flush()

    print(order)

    time.sleep(1)