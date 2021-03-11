import pyodbc


class DbConnection:

    def dbConnect(self):
        conn = pyodbc.connect(r'Driver=SQL Server;Server=.\SQLEXPRESS;Database=master;Trusted_Connection=yes;')
        cursor = conn.cursor()
        return cursor

