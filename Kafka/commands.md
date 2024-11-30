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
# Exercise 2 - Explore partitions and consumer groups
Create a topic-2 with 3 partitions
```
bin/kafka-topics.sh --create \
--topic task2-topic \
--bootstrap-server localhost:9092 \
--partitions 3 \
--replication-factor 1

```
### Analysis
* When 1, 2 or 3 consumers are actively listening on the consumer group, they receive messages once at a time
* When a fourth consumer is introduced, one of the consumers will stay idle until one of the consumers dies out.
  

# Exercise 3 - Multi-Topic Producer and Consumer with Consumer Groups
Create the purchase-topic
```
bin/kafka-topics.sh --create \
--topic purchase-topic \
--bootstrap-server localhost:9092 \
--partitions 3 \
--replication-factor 1
```
Create user-activity-topic
```
bin/kafka-topics.sh --create \
--topic user-activity-topic \
--bootstrap-server localhost:9092 \
--partitions 3 \
--replication-factor 1
```
In project folder, create the multi-topic producer process and group consumers
```
pyton3 task3/producer.py
```
```
pyton3 task3/activity-consumer.py
```
```
pyton3 task3/purchase-consumer.py
```

