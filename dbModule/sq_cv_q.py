from dbModule import DBConnection as dbClass

class sq_cv_q:
    db = ''
    cursor = ''

    def __init__(self):
        conn = dbClass.DBConnection()
        self.db = conn.getConnection()
        self.cursor = self.db.cursor()

    def getAll(self):
        sql = "SELECT * FROM cv_q"
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(e)
            self.db.rollback()



    def getDataForNbDataset(self):
        sql = "SELECT id, age, skills, currentjob, experience_yrs, university, degree, specialization, salary FROM cv_q WHERE nbstatus=0"
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(e)
            self.db.rollback()

    def updateNbStatus(self, id):
        sql = "UPDATE cv_q SET nbstatus=1 WHERE id=%s"
        try:
            self.cursor.execute(sql, id)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()





    def getDataForDtDataset(self):
        sql = "SELECT id, age, skills, currentjob, experience_yrs, university, degree, specialization, salary FROM cv_q WHERE dtstatus=0"
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(e)
            self.db.rollback()

    def updateDtStatus(self, id):
        sql = "UPDATE cv_q SET dtstatus=1 WHERE id=%s"
        try:
            self.cursor.execute(sql, id)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()