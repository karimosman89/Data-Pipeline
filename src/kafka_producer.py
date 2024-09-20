from kafka import KafkaProducer
import json
import time

def produce_messages():
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    for i in range(100):
        message = {'id': i, 'value': i * 2}
        producer.send('test_topic', value=message)
        time.sleep(1)  # Simulate delay

if __name__ == "__main__":
    produce_messages()

