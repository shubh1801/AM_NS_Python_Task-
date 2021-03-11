from src.ImageConvertor import *
from kafka import KafkaConsumer
import json

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'python',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:
        message = message.value
        print('{} added to'.format(message))

    imgc = ImageConvertor()
    imgc.rgb2gray('D:/DSC_6462 02.jpg')


