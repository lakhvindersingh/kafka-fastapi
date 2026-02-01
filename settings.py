from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Kafka FastAPI App"

    # Kafka
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"

    USER_SIGNUP_TOPIC: str = "user-signup"

    class Config:
        env_file = ".env"


settings = Settings()
