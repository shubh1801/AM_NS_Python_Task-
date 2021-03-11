import cv2
import os
from src.DbConnection import *
import uuid
import datetime


# rgb2gray is method to convert income image via image path
# rgb_file_path - as input argument to method - rgp image path on local machine

class ImageConvertor:

    def rgb2gray(self, rgb_file_path: str):
        image = cv2.imread(rgb_file_path)
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        output_file_name = os.path.join(os.getcwd(), "src\\Output\\"+str(uuid.uuid4())+".jpg")
        cv2.imwrite(output_file_name, gray)

        dbc = DbConnection()
        conn = dbc.dbConnect()
        cursor = conn.cursor()
        current_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        cursor.execute("""insert into consumer_records (consumer_id,distributer_id,save_path,time_processed) values ('121','123','""" + output_file_name + """','""" + current_time + """')""")
        conn.commit()

