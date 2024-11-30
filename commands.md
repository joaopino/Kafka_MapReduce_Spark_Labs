pip install git+https://github.com/dpkp/kafka-python.git

### Activate the Zookeper
```
zkServer.sh start  
```

## Start the Kafka Broker
```
cd
cd kafka-3.9.0-src/
bin/kafka-server-start.sh config/server.properties
```

# Exercise 1 - Producer and Consumer 
Note: change the directory to the Project 2 directory

- Terminal 1
```
source venv/bin/activate
python3 consumer.py
```
- Terminal 2
```
source venv/bin/activate
python3 producer.py
```

Create a topic-2 with 3 partitions
```
bin/kafka-topics.sh --create \
--topic task2-topic \
--bootstrap-server localhost:9092 \
--partitions 3 \
--replication-factor 1

```