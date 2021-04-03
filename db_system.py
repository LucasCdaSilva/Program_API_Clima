
import psycopg2 as db


class PostgresDB():
    _db_postgres = None

    def __init__(self, mhost, dbase, usr, pwd):
        self._db_postgres = db.connect(host=mhost, database=dbase, user=usr,  password=pwd)
        
    def command(self, sql=""):
        cur=self._db_postgres.cursor()
        cur.execute(self.sql)
        cur.close()
        self._db_postgres.commit()
        

    def consultar(self, sql=""):
        rs=None
        cur=self._db_postgres.cursor()
        cur.execute(sql)
        rs=cur.fetchall()

    def fechar(self):
        self._db_postgres.close()
