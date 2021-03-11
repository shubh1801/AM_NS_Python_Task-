import pyodbc

#Using Local Microsoft SQL Server
#user windows credential for authentication

class DbConnection:

    def dbConnect(self):
        conn = pyodbc.connect(r'Driver=SQL Server;Server=.\SQLEXPRESS;Database=master;Trusted_Connection=yes;')
        return conn

