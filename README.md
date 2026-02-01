# Kafka FastAPI Project

A high-performance asynchronous event-driven application built with FastAPI and Apache Kafka.

## Features

- 🚀 **FastAPI**: Modern, fast (high-performance) web framework.
- 📨 **Kafka Integration**: Asynchronous messaging with Kafka producers and consumers.
- ⚡ **Real-time**: Event-driven architecture for scalable processing.
- 🛠 **Pydantic V2**: Data validation and settings management.

## Project Structure

```
kafka-proj/
├── api/
│   └── routes.py       # API endpoints and routing
├── messaging/
│   ├── consumer.py     # Kafka consumer implementation
│   ├── producer.py     # Kafka producer implementation
│   └── topics.py       # Kafka topic definitions
├── schemas/
│   └── events.py       # Pydantic models for events
├── services/
│   └── user_service.py # Business logic
├── main.py             # Application entry point
├── settings.py         # Configuration management
└── requirements.txt    # Project dependencies
```

## Prerequisites

- **Python 3.11+**
- **Apache Kafka** (running locally or via Docker)
- **Zookeeper** (if using older Kafka versions)

## Installation

1. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Ensure your Kafka broker is running at `localhost:9092` (default). 
You can configure the application using environment variables or by modifying `settings.py`.

## Running the Application

Start the FastAPI server:

```bash
python main.py
```

The server will start at `http://127.0.0.1:8000`.

### API Documentation

Interactive API documentation is available at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Testing the Endpoint

Send a POST request to `/signup` to publish an event:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/signup' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_id": "user_123",
  "email": "user@example.com",
  "timestamp": "2024-01-01T12:00:00"
}'
```

## Running Consumers

To consume messages from the topic, run the consumer module in a separate terminal:

```bash
python -m messaging.consumer
```

## 🐳 Docker Deployment (Recommended for Production)

For a production-ready setup, use Docker Compose to orchestrate the application, consumer, and Kafka cluster.

1. **Start all services**:
   ```bash
   docker-compose up --build -d
   ```
   This will start:
   - **Zookeeper**: Coordinator for Kafka.
   - **Kafka**: The message broker.
   - **Backend**: FastAPI app on port 8000.
   - **Worker**: The consumer process (restarts automatically if it crashes).

2. **Check Logs**:
   ```bash
   docker-compose logs -f worker
   ```

3. **Stop services**:
   ```bash
   docker-compose down
   ```

## 🏗️ Production Best Practices for Large Projects

1.  **Use a Framework**: For complex consumers, use libraries like **FastStream** or **Faust**. They handle:
    -   Automatic retries & Dead Letter Queues (DLQ).
    -   Batch processing.
    -   AsyncIO native support.
    
    *Example FastStream snippet:*
    ```python
    from faststream import FastStream
    from faststream.kafka import KafkaBroker
    
    broker = KafkaBroker("localhost:9092")
    app = FastStream(broker)
    
    @broker.subscriber("user-signup")
    async def process_signup(msg: dict):
        # business logic
    ```

2.  **Schema Registry**: Use Confluent Schema Registry to enforce data contracts (Avro/Protobuf) between producers and consumers.

3.  **Observability**: Integrate OpenTelemetry to trace requests from API -> Kafka -> Consumer.

4.  **Error Handling**: Always implement a retry mechanism with exponential backoff for failed messages.

