import json
import random
import time
from datetime import datetime

from kafka import KafkaProducer

# Initialize KafkaProducer to send messages to Kafka topic 'face.embed.data'
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

emotions = ['happy', 'sad', 'angry', 'surprised', 'neutral']
genders = ['male', 'female', 'other']


def generate_random_data():
    return {
        'age': random.randint(10, 80),
        'emotion': random.choice(emotions),
        'gender': random.choice(genders),
        'timestamp': datetime.now().isoformat()
    }


while True:
    data = generate_random_data()
    producer.send('face.embed.data', value=data)
    print(f"Sent data: {data}")
    time.sleep(1)
