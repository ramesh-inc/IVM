from dbModule import DBConnection as dbClass

class sq_dt_prediction:
    db = ''
    cursor = ''

    def __init__(self):
        conn = dbClass.DBConnection()
        self.db = conn.getConnection()
        self.cursor = self.db.cursor()

    def getCountRowsPrediction(self, userid):
        sql = "SELECT COUNT(id) FROM dt_prediction WHERE userid=%s"
        try:
            self.cursor.execute(sql, userid)
            result = self.cursor.fetchone()
            return result[0]
        except Exception as e:
            print(e)
            self.db.rollback()

    def setPredictionExpValue(self, id, exp, precentage):
        sql = "INSERT INTO dt_prediction(userid, jobPrediction, jobPrecentage) VALUES (%s, %s, %s)"
        try:
            self.cursor.execute(sql, (id, exp, precentage))
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    def updatePredictionExpValue(self, id, exp, precentage):
        sql = "UPDATE dt_prediction SET jobPrediction=%s, jobPrecentage=%s WHERE userid=%s"
        try:
            self.cursor.execute(sql, (exp, precentage, id))
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    def getPredictionExp(self, userid):
        sql = "SELECT jobPrediction FROM dt_prediction WHERE userid=%s"
        try:
            self.cursor.execute(sql, userid)
            result = self.cursor.fetchone()
            return result[0]
        except Exception as e:
            print(e)
            self.db.rollback()

    def setPredictionSalValue(self, id, sal, precentage):
        sql = "INSERT INTO dt_prediction(userid, salary, salPrecentage) VALUES (%s, %s, %s)"
        try:
            self.cursor.execute(sql, (id, sal, precentage))
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    def updatePredictionSalValue(self, id, sal, precentage):
        sql = "UPDATE dt_prediction SET salary=%s, salPrecentage=%s WHERE userid=%s"
        try:
            self.cursor.execute(sql, (sal, precentage, id))
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()



    def getMatchingByUserId(self, userid):
        sql = "SELECT jobPrediction, jobPrecentage FROM dt_prediction WHERE userid=%s"
        try:
            self.cursor.execute(sql, userid)
            results = self.cursor.fetchone()
            return results
        except Exception as e:
            print(e)
            self.db.rollback()