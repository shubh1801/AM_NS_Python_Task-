import cv2
import os
import json
from kafka import KafkaProducer
from kafka.errors import kafka_errors
from src.DbConnection import *
import base64
import datetime
import pickle

file_full_path = 'D:\DSC_6462 02.jpg'


producer = KafkaProducer(bootstrap_servers=['localhost:9092']
                         #value_serializer=lambda v: (v.encode('utf-8'))
                          )
dbc = DbConnection()
conn = dbc.dbConnect()
cursor = conn.cursor()

directory = os.path.join(os.getcwd(), "Input")

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        file_full_path = os.path.join(directory, filename)
        # Tried to send the Image by converting it into Byte Stream but failed to do it
        img = cv2.imread(file_full_path)
        sucess, en_img = cv2.imencode(".jpg", img)
        print(sucess)
        print(en_img)

        var = producer.send("topicamns", pickle.dumps(en_img))
        try:
            record_metadata = var.get(timeout=10)
        except kafka_errors as e:
            print(e)

        # # Adding Record into Database
        # current_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        #
        # cursor.execute(
        #     """insert into distributer_records (distributer_id,file_name,time_received) values ('123','""" + file_full_path + """' , '""" + current_time + """')""")
        # conn.commit()




