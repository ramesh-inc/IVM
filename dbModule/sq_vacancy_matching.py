from dbModule import DBConnection as dbClass

class sq_vacancy_matching:
    db = ''
    cursor = ''

    def __init__(self):
        conn = dbClass.DBConnection()
        self.db = conn.getConnection()
        self.cursor = self.db.cursor()

    def setCvForJobVacancy(self, id, userid, nbValue, dtValue):
        sql = "INSERT INTO vacancy_matching(userid, vacid, nbmatching, dtmatching) VALUES (%s, %s, %s, %s)"
        try:
            self.cursor.execute(sql, (userid, id, nbValue, dtValue))
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    def getCountId(self, id, userid):
        sql = "SELECT COUNT(id) FROM vacancy_matching WHERE vacid=%s AND userid=%s"
        try:
            self.cursor.execute(sql, (id, userid))
            result = self.cursor.fetchone()
            return result[0]
        except Exception as e:
            print(e)
            self.db.rollback()

    def selectByResumeID(self, userid):
        sql = "SELECT * FROM vacancy_matching WHERE userid=%s"
        try:
            self.cursor.execute(sql, userid)
            result = self.cursor.fetchall()

            return result

        except Exception as e:
            print(e)
            self.db.rollback()

    def selectByVacancyID(self, vacancyid):
        sql = "SELECT * FROM vacancy_matching WHERE vacid=%s"
        try:
            self.cursor.execute(sql, vacancyid)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            self.db.rollback()