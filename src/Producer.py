from time import sleep
import json
from kafka import KafkaProducer
import cv2



buffer_frame1 = cv2.imread('D:/DSC_6462 02.jpg')

producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))

event = {"Image_Name": "Image1",
         "File_Type": "jpg",
         "Byte_Array": str(buffer_frame1.tobytes())}

producer.send("python", event)

