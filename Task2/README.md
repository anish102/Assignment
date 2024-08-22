# Django Kafka Integration Project

This project is a Django-based system that integrates with Apache Kafka to handle real-time data generation, storage, and retrieval via a REST API.

## Features

- **Kafka Producer:** Generates random data and publishes it to a Kafka topic.
- **Kafka Consumer:** Listens to the Kafka topic and stores the data in the Django database.
- **Django Model:** Stores the incoming data from Kafka.
- **REST API:** Provides an endpoint to retrieve the stored data in JSON format.

## Requirements
The kafka server should be installed and configured from the [link](https://kafka.apache.org/quickstart).
The zookeper and kafka server must be started from the directory where kafka is installed

For other requirements, you can directly install required packages from following command:
pip install -r requirements.txt

## Running
After completing the setup, first the zookeper server should be started with command: bin/zookeeper-server-start.sh config/zookeeper.properties
Then, the kafka server should be started: bin/kafka-server-start.sh config/kraft/server.properties
Start the django server: python manage.py runserver
Make migrations: python manage.py make-migrations
                 python manage.py migrate
Then, run the kafka_producer.py file for producing data: python kafka_producer.py.
The, run_kafka_consumer.py should also be run to get data produced by producer: python manage.py run_kafka_consumer


## API
To see the api response, one can go to 127.0.0.1:8000/api/face_embed.
The data is shown in the json format.