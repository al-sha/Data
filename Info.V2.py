# SQLITE is used for small applications.

import sqlite3


class Employee:
    def __init__(self):
        self.conn = sqlite3.connect('info.db')
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS info (ID INTEGER, Name TEXT, Salary INTEGER)")

        self.choose = int(input("Please enter 1 To add a new record or 2 To delete an existing record: "))

        if self.choose == 1:
            self.insert()
        elif self.choose == 2:
            self.delete()


    def insert(self):
        self.Id = int(input("Please enter ID: "))
        self.Name = str(input("Please Enter Name: "))
        self.Salary = int(input("Please enter Salary: "))

        self.c.execute("INSERT INTO info (Id, Name, Salary) VALUES (?, ?, ?)", (self.Id, self.Name, self.Salary))
        self.conn.commit()
        self.c.close
        self.conn.close()

    def delete(self):

        self.delete_Id = int(input("Please enter an ID to delete: "))


        self.c.execute('DELETE FROM info WHERE Id = ' + str(self.delete_Id))
        self.conn.commit()
        self.c.close
        self.conn.close()



emp1 = Employee()

input("Press enter to exit....")

