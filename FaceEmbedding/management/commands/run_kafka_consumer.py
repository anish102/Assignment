# run_kafka_consumer.py
import json

from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from FaceEmbedding.models import FaceEmbed
from kafka import KafkaConsumer


class Command(BaseCommand):
    help = 'Runs the Kafka consumer to process messages and store them in the database.'

     # Initialize KafkaConsumer to read messages from the 'face.embed.data' topic and save data in database
    def handle(self, *args, **kwargs):
        consumer = KafkaConsumer(
            'face.embed.data',
            bootstrap_servers='localhost:9092',
            auto_offset_reset='earliest',
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )

        self.stdout.write(self.style.SUCCESS('Started Kafka consumer'))

        for message in consumer:
            data = message.value
            face_embed = FaceEmbed(
                age=data['age'],
                emotion=data['emotion'],
                gender=data['gender'],
                timestamp=data['timestamp']
            )
            face_embed.save()
            self.stdout.write(self.style.SUCCESS(f"Saved data: {data}"))
