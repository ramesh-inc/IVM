from dbModule import DBConnection as dbClass

class sq_vacancies:
    db = ''
    cursor = ''
    tempVal = []

    def __init__(self):
        conn = dbClass.DBConnection()
        self.db = conn.getConnection()
        self.cursor = self.db.cursor()

    def getLiveVacenciesById(self, vacencyId):
        sql = "SELECT v_id, job FROM vacancies WHERE status=0 AND v_id=%s"
        try:
            self.cursor.execute(sql, vacencyId)
            results = self.cursor.fetchone()
            return results
        except Exception as e:
            print(e)
            self.db.rollback()

    def getLiveVacenciesByName(self, vacency):
        sql = "SELECT v_id, job FROM vacancies WHERE status=0 AND job=%s"
        try:
            self.cursor.execute(sql, vacency)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(e)
            self.db.rollback()

    def insertVacancy(self, company_id, job, education, experience, ex_year, skills, other_skills):

        sql = "insert into vacancies(company_id, job, education, experience, ex_year, skills, other_skills) values(%s, %s, %s, %s, %s, %s, %s)"
        try:
            self.cursor.execute(sql, (company_id, job, education, experience, ex_year, skills, other_skills))
            self.db.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)
            self.db.rollback()

    def selectVacancies(self, vac_id):
        sql = "SELECT * FROM vacancies WHERE v_id=%s"
        try:
            self.cursor.execute(sql, vac_id)
            result = self.cursor.fetchall()

            return result

        except Exception as e:
            print(e)
            self.db.rollback()