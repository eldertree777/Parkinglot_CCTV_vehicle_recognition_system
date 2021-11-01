# Module Imports
import mariadb
import sys

class DB:
    # Connect to MariaDB Platform
    def __init__(self):
        try:
            self.conn = mariadb.connect(
                user="root",
                password="justghkdwp!2",
                host="127.0.0.1",
                port=3306,
                database="parkinglot"

            )

            # Get Cursor
            self.cur = self.conn.cursor()

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

    def insertData(self,date,loc,space,car):
        sql = "INSERT INTO cctv VALUES ('" + date + "', '" +loc + " ', " + space + "," +car+")"
        self.cur.execute(sql)


    