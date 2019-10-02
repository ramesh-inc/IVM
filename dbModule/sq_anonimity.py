from dbModule import DBConnection as dbClass


class anonimity:
    db = ''
    cursor = ''

    def __init__(self):
        conn = dbClass.DBConnection()
        self.db = conn.getConnection()
        self.cursor = self.db.cursor()

    def insertAnonimity(self, userid, a_name, a_address, a_nic, a_email, a_phone):

        sql = "insert into ivm_anonimyzation(user_id, name, email, address, phone, nic) values(%s, %s, %s, %s, %s, %s)"
        try:
            self.cursor.execute(sql, (userid, a_name, a_email, a_address, a_phone, a_nic))
            self.db.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)
            self.db.rollback()

    def selectByUserID(self, userid):
        sql = "SELECT * FROM ivm_anonimyzation WHERE user_id=%s"
        try:
            self.cursor.execute(sql, userid)
            result = self.cursor.fetchall()

            return result

        except Exception as e:
            print(e)
            self.db.rollback()