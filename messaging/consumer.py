from kafka import KafkaConsumer
import json
from services.user_service import process_signup

from messaging.topics import USER_SIGNUP_TOPIC
from settings import settings

consumer = KafkaConsumer(
    USER_SIGNUP_TOPIC,
    bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
    group_id="user-service",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"Starting consumer for topic: {USER_SIGNUP_TOPIC}")

for msg in consumer:
    try:
        logger.info(f"Received message: {msg.value}")
        process_signup(msg.value)
    except Exception as e:
        logger.error(f"Error processing message: {e}")
