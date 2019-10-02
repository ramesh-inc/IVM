from dbModule import DBConnection as dbClass


class company:
    db = ''
    cursor = ''

    def __init__(self):
        conn = dbClass.DBConnection()
        self.db = conn.getConnection()
        self.cursor = self.db.cursor()

    def insertCompany(self, company_name, address, phone, email, job_type):

        sql = "insert into company(company_name, address, phone, email, job_type) values(%s, %s, %s, %s, %s)"
        try:
            self.cursor.execute(sql, (company_name, address, phone, email, job_type))
            self.db.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)
            self.db.rollback()