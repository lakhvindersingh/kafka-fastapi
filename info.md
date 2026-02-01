# Kafka Setup & Usage Guide

## 1. Prerequisites (Windows Local Setup)
*   **JDK**: Install Java Development Kit (JDK) 11+ from the [Oracle website](https://www.oracle.com/java/technologies/downloads/).
*   **Kafka**: Download the binary tar file from [Apache Kafka](https://kafka.apache.org/downloads) and extract it (e.g., to `C:\kafka`).
    *   Binaries: `C:\kafka\bin`
    *   Config: `C:\kafka\config`

## 2. Kraft Mode (No Zookeeper)
Modern Kafka versions (3.3+) verify Kraft mode, which removes the need for Zookeeper.
*   Ensure you are using config files from the `config/kraft` directory.
*   Note: `zookeeper-server-start.bat` is **not needed**.

## 3. Storage Formatting
You must generate a unique Cluster ID and format your storage directories before starting Kafka.

**Generate Cluster ID:**
```powershell
cd C:\kafka\bin\windows
.\kafka-storage.bat random-uuid
# Example Output: ZlCmyEihTdCvN9ZSs7yZGw
```

**Format Log Directories:**
Use the generated UUID to format the storage (replace `UUID` with your actual ID):
```powershell
.\kafka-storage.bat format `
  -t ZlCmyEihTdCvN9ZSs7yZGw `
  -c ..\..\config\kraft\server.properties
```

## 4. Start Kafka Server
Run the Kafka broker using the Kraft configuration:
```powershell
cd C:\kafka\bin\windows
.\kafka-server-start.bat ..\..\config\kraft\server.properties
```

## 5. Manage Topics

**List Topics:**
```powershell
.\kafka-topics.bat --bootstrap-server localhost:9092 --list
```

**Create a Topic:**
```powershell
.\kafka-topics.bat --bootstrap-server localhost:9092 --create --topic test --partitions 1 --replication-factor 1
```

## 6. Test with Console Tools

**Start Producer (Send Messages):**
```powershell
.\kafka-console-producer.bat --bootstrap-server localhost:9092 --topic test
```

**Start Consumer (Read Messages):**
```powershell
.\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic test --from-beginning
```

## 7. Docker Clean Up
If simulating a fresh environment with Docker:

**Reset & Restart:**
```powershell
docker-compose down -v
docker-compose up --build -d
```

**Monitor Logs:**
```powershell
docker-compose logs -f
```
