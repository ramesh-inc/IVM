from dbModule import DBConnection as dbClass


class user:
    db = ''
    cursor = ''

    def __init__(self):
        conn = dbClass.DBConnection()
        self.db = conn.getConnection()
        self.cursor = self.db.cursor()

    def insertUser(self, age, name, address, nic, email, phone):

        sql = "insert into user(age, name, address, nic, email, phone) values(%s, %s, %s, %s, %s, %s)"
        try:
            self.cursor.execute(sql, (age, name, address, nic, email, phone))
            self.db.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)
            self.db.rollback()

    def selectUser(self, userid):
        sql = "SELECT * FROM user WHERE id=%s"
        try:
            self.cursor.execute(sql, userid)
            result = self.cursor.fetchall()
            # for row in result:
            #     print("{0} {1} {2}".format(row[0], row[1], row[2]))

            return result

        except Exception as e:
            print(e)
            self.db.rollback()