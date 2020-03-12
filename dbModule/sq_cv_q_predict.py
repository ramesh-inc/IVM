from dbModule import DBConnection as dbClass

class cv_q_predict:
    db = ''
    cursor = ''

    def __init__(self):
        conn = dbClass.DBConnection()
        self.db = conn.getConnection()
        self.cursor = self.db.cursor()

    def getDataForNbPrediction(self):
        sql = "SELECT id, userid, age, skills, experience_yrs, university, degree, specialization FROM cv_q_predict WHERE nbstatus=1"
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(e)
            self.db.rollback()

    def updateNbStatus(self, id):
        sql = "UPDATE cv_q_predict SET nbstatus=1 WHERE id=%s"
        try:
            self.cursor.execute(sql, id)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()



    def getDataForDtPrediction(self, id):
        sql = "SELECT id, userid, age, skills, experience_yrs, university, degree, specialization FROM cv_q_predict WHERE dtstatus=1 AND id=%s"
        try:
            self.cursor.execute(sql, id)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(e)
            self.db.rollback()

    def updateDtStatus(self, id):
        sql = "UPDATE cv_q_predict SET dtstatus=1 WHERE id=%s"
        try:
            self.cursor.execute(sql, id)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    def insertPredictionData(self, userid, age, skills, projects, exp_yrs, university, degree, specialization, obj):

        sql = "insert into cv_q_predict(userid,age,skills,projects,experience_yrs,university,degree,specialization,objectives) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            self.cursor.execute(sql, (userid, age, skills, projects, exp_yrs, university, degree, specialization, obj))
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()