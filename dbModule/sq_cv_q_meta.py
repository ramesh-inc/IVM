from dbModule import DBConnection as dbClass

class sq_cv_q_meta:
    db = ''
    cursor = ''

    def __init__(self):
        conn = dbClass.DBConnection()
        self.db = conn.getConnection()
        self.cursor = self.db.cursor()

    def getAll(self):
        sql = "SELECT metakey, metavalue FROM cv_q_meta"
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(e)
            self.db.rollback()

    def getMetaKeys(self):
        tempVal = []
        sql = "SELECT metakey FROM cv_q_meta"
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()

            for row in results:
                tempVal.append(row[0])

            return tempVal

        except Exception as e:
            print(e)
            self.db.rollback()

    def getMetaValue(self, key):
        tempVal = ''
        sql = "SELECT metavalue FROM cv_q_meta WHERE metakey=%s"
        try:
            self.cursor.execute(sql, (key))
            results = self.cursor.fetchall()

            for row in results:
                tempVal = row[0]

            return tempVal
        except Exception as e:
            print(e)
            self.db.rollback()