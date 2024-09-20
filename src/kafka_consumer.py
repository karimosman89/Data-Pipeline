from kafka import KafkaConsumer
import json

def consume_messages():
    consumer = KafkaConsumer('test_topic',
                             bootstrap_servers='localhost:9092',
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')),
                             auto_offset_reset='earliest')
    
    for message in consumer:
        print(f"Received: {message.value}")

if __name__ == "__main__":
    consume_messages()

