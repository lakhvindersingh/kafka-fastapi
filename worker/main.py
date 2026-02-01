from faststream import FastStream
from faststream.kafka import KafkaBroker
from messaging.topics import USER_SIGNUP_TOPIC
from schemas.events import UserSignupEvent
from settings import settings
import logging

# Configure structured logging (best practice for production)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize Broker with settings
broker = KafkaBroker(settings.KAFKA_BOOTSTRAP_SERVERS)

# Initialize FastStream App
app = FastStream(broker)

# Publisher example (if this service also emits events)
# to_topic = broker.publisher("processed_events")

@broker.subscriber(USER_SIGNUP_TOPIC)
async def handle_user_signup(event: UserSignupEvent):
    """
    Process user signup events with automatic Pydantic validation.
    FastStream automatically deserializes the JSON body into the UserSignupEvent model.
    """
    logger.info(f"Received signup event for user: {event.user_id} ({event.email})")
    
    # Simulate async business logic processing
    try:
        await process_business_logic(event)
        logger.info(f"Successfully processed signup for {event.user_id}")
    except Exception as e:
        logger.error(f"Failed to process signup for {event.user_id}: {e}")
        # In a real app, you might want to raise the exception to trigger retry 
        # or dead-letter queue mechanisms if configured.
        raise e

async def process_business_logic(event: UserSignupEvent):
    # Place your actual service calls here (e.g., database, email service)
    # await user_service.create_user(event)
    pass
