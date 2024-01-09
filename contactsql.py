import sqlite3
class database:
    def _init_(self,db):
        try:
            self.con=sqlite3.connect(db)
            self.c=self.con.cursor()
            self.c.execute(""" CREATE TABLE IF NOT EXISTS datas( pid INTEGER PRIMARY KEY ,
                           name TEXT NOR NULL,
                           contact TEXT NOR NULL)
                            """)
            self.con.commit()
            print("Table Created Successfully ")
        except Exception as e:
            print("error:",e)
        def insert_record(self):
            name=input("Enter your name:")
            contact=input("Enter your contact:")
            sql="""
                   INSERT INTO datas VALUES(NULL,?,?)
                   """
            self.c.execute(sql(name,contact))
            self.con.commit()
            print("Record added successfully")
        def fetch_record(self):
            self.c.execute("SELECT * FROM datas")
            data=self.c.fetchall()
            print("\n")
            print("List of Records")
            for datas in data:
                print("datas")
        def update_records(self):
            print("1.Name")
            print("2.Contact")
            option=int(input("\n which field you wnat to update:"))
            pid=input("Enter your id:")
            if option == 1:
                name-input("Enter your name:")
                sql="""update datas set name=? where pid=?"""
                self.c.execute(sql,(name,pid))
                self.con.commit()
                obj.fetch_record()
                print("\n")
                print("update successfully")
            elif option == 2:
                contact=input("Enter your contact:")
                sql="""update datas set contact=? where pid=?"""
                self.c.execute(sql,(contact,pid))
                self.con.commit()
                obj.fetch_record()
                print("\n")
                print("update successfully")
            else:
                print("Invalid")
        def remove_record(self):
            pid=input("Enter your id:")
            sql="delete from datas where pid=?"
            self.c.execute(sql,(pid))
            self.con.commit()
            obj.fetch_record()
            print("\n")
            print("Record deleted successfully")
obj=database("database.db")
while True:
    print("\n")
    print("1.INSERT RECORD")
    print("2.FETCH RECORD/")
    print("3.UPDATE RECORD")
    print("4.DELETE RECORD")
    print("\n")

    option=int(input("enter your options     :"))

    if option == 1:
        obj.insert_record()
    elif option == 2:
        obj.fetch_record()
    elif option == 3:
        obj.update_record()
    elif option == 4:
        obj.remove_record()
    else:
        quit()