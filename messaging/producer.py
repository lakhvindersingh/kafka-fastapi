from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v, default=str).encode("utf-8")
)

def send_event(topic: str, data: dict):
    producer.send(topic, data)
    producer.flush()
