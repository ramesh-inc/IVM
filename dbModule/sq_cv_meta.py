from dbModule import DBConnection as dbClass

class sq_cv_meta:
    db = ''
    cursor = ''
    tempVal = []

    def __init__(self):
        conn = dbClass.DBConnection()
        self.db = conn.getConnection()
        self.cursor = self.db.cursor()

    def getMetaValue(self, key):
        self.tempVal = []
        sql = "SELECT metavalue FROM cv_meta WHERE metakey=%s"
        try:
            self.cursor.execute(sql, (key))
            results = self.cursor.fetchall()

            for row in results:
                self.tempVal.append(row[0])

            return self.tempVal
        except Exception as e:
            print(e)
            self.db.rollback()

    def setMetaKey(self, meta_key, meta_value):
        sql = "INSERT INTO cv_meta(metakey, metavalue) VALUES (%s,%s)"
        try:
            self.cursor.execute(sql, (meta_key, meta_value))
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    def updateMetaValue(self, meta_key, meta_value):
        sql = "UPDATE cv_meta SET metavalue=%s WHERE metakey=%s"
        try:
            self.cursor.execute(sql, (meta_value, meta_key))
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    def getCountMetaKey(self, meta_key):
        sql = "SELECT COUNT(metakey) FROM cv_meta WHERE metakey=%s"
        try:
            self.cursor.execute(sql, meta_key)
            results = self.cursor.fetchone()
            return results[0]
        except Exception as e:
            print(e)
            self.db.rollback()