import sqlite3

class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS students(
            id Integer Primary key,
            name text,
            email text,
            gender text,
            gpa text 
        )

        """
        self.cur.execute(sql)
        self.con.commit()
    def insert(self,id,name,email,gender,gpa):
        self.cur.execute("insert into students values (?,?,?,?,?)",
        (id,name,email,gender,gpa))
        self.con.commit()
        
    def fetch(self):
        self.cur.execute("SELECT * FROM students")
        rows=self.cur.fetchall()
        return rows

    def remove(self,id):
        self.cur.execute("delete from students where id=?",(id,))
        self.con.commit()

    def update(self,id,name,email,gender,gpa):
        self.cur.execute("update students set name=?,email=?,gender=?,gpa=? where id=?",
        (name,email,gender,gpa,id))
        self.con.commit()

