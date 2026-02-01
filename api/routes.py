from fastapi import APIRouter
from schemas.events import UserSignupEvent
from messaging.producer import send_event
from messaging.topics import USER_SIGNUP_TOPIC

router = APIRouter()

@router.post("/signup")
def signup(event: UserSignupEvent):
    send_event(USER_SIGNUP_TOPIC, event.model_dump())
    return {"status": "event published"}
