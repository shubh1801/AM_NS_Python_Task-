from src.ImageConvertor import *
from kafka import KafkaConsumer
import json
import os
import cv2
import pickle

imgc = ImageConvertor()

if __name__ == '__main__':

    directory = os.path.join(os.getcwd(), "src\\Input")
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            file_full_path = os.path.join(directory, filename)
            imgc.rgb2gray(file_full_path)



            # consumer = KafkaConsumer(
            #     'topicamns',
            #     bootstrap_servers=['localhost:9092'],
            #     auto_offset_reset='earliest',
            #     enable_auto_commit=True,
            #     group_id='my-group',
            #     #value_deserializer=lambda x: (x.decode('utf-8'))
            # )
            #
            # for message in consumer:
            #     message = message.value
            #     #imgc.rgb2gray(file_full_path)
            #     print(message)
            #     print(type(message))
            #     try:
            #         y = pickle.loads(message)
            #         print(y)
            #         cv2.("new.jpg",y)
            #         cv2.imshow("image",y)
            #     except Exception as e:
            #         print(e)








