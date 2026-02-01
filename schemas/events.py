from pydantic import BaseModel
from datetime import datetime

class UserSignupEvent(BaseModel):
    user_id: str
    email: str
    timestamp: datetime
