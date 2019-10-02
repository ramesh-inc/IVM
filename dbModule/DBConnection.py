import pymysql

class DBConnection:

    def __init__(self):
        self.db = pymysql.connect("localhost","root","","ivm-madhushani")

    def getConnection(self):
        return self.db