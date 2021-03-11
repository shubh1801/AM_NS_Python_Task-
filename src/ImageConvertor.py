import cv2
from src.DbConnection import *


class ImageConvertor:

    def rgb2gray(self, rgbfilepath: str):
        image = cv2.imread(rgbfilepath)
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        cv2.imwrite('D:/gray.jpg', gray)

        dbc = DbConnection()
        cursor = dbc.dbConnect()
        cursor.execute('SELECT * FROM dbo.raw_bank_transaction')
        for row in cursor:
            print(row)

# cursor.execute("insert into distributer_records (distributer_id) values ('123')")
# conn.commit()
