# Activate and setup the python virtual environment
```
python3.10 -m venv python3_10_venv
source python3_10_venv/bin/activate
pip install mrjob
```

# Exercise 1 - Average Number of Friends by Age
```
python3 MapReduce/Task_1/task1.py MapReduce/Task_1/fakefriends.csv
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

