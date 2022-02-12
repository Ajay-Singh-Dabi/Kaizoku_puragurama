import mysql.connector as connector

"""
This class DBHelper is used to create the database which
will contain the data of the existing employees and
directors
"""

class DBHelper:
    def __init__(self):
        self.con1 = connector.connect(host='localhost',
                                      port='3306',
                                      user='root',
                                      password='##Ajay2000@##',
                                      database='existing_database')
        #
        # print(con1)
        query1 = 'create table if not exists directors(userId int primary key,Dname varchar(20) NOT NULL,' \
                 'contact varchar(10) NOT NULL,email varchar(40) NOT NULL,officeNo int NOT NULL,' \
                 ' photo varchar(50) NOT NULL,start_time int NULL, end_time int NOT NULL)'

        query2 = 'create table if not exists employee(userId int primary key,Dname varchar(20) NOT NULL,' \
                 'contact varchar(10) NOT NULL,email varchar(40) NOT NULL,officeNo int NOT NULL,a' \
                 ' photo varchar(50) NOT NULL,start_time int NULL, end_time int NOT NULL)'

        query3 = 'create table if not exists access_table(userId int,Dname varchar(20) NOT NULL,' \
                 'roomNo int NOT NULL,' \
                 'foreign key (userId) references employee(userId))'
        cur = self.con1.cursor()
        cur.execute(query1)
        cur.execute(query2)
        cur.execute(query3)
        print('Created')

    #Insert

    def insert_access_table(self, User_Id, User_Name, Room_number):
        query = "insert into access_table(userId,Dname,roomNo)" \
                " values({},'{}',{})".format(User_Id,
                                             User_Name,
                                             Room_number)
        print(query)
        cur = self.con1.cursor()
        cur.execute(query)
        self.con1.commit()
        print("Done Inserting in Access Table")

    def insert_data(self, User_Id, User_Name, Contact, email,office_no, photo, start_time, end_time, table_name):
        if table_name == "directors":
            query = "insert into directors(userId,Dname,contact,email,officeNo,photo,start_time,end_time)" \
                    " values({},'{}','{}','{}',{},'{}',{},{})".format(User_Id,
                                                                   User_Name,
                                                                   Contact,
                                                                   email,
                                                                   office_no,
                                                                   photo,
                                                                   start_time,
                                                                   end_time)
            print(query)
            cur = self.con1.cursor()
            cur.execute(query)
            self.con1.commit()
            print("Done Inserting in Director Table")

        if table_name == "employee":
            query = "insert into employee(userId,Dname,contact,email,officeNo,photo,start_time,end_time)" \
                    " values({},'{}','{}','{}',{},'{}',{},{})".format(User_Id,
                                                                   User_Name,
                                                                   Contact,
                                                                   email,
                                                                   office_no,
                                                                   photo,
                                                                   start_time,
                                                                   end_time)
            print(query)
            cur = self.con1.cursor()
            cur.execute(query)
            self.con1.commit()
            print("Done Inserting in Employee Table")

    def Pull_Data(self):
        query = "select * from employee"
        cur = self.con1.cursor()
        cur.execute(query)
        for row in cur:
            print(row)


"""
This class PushHepler is used to create the database 
in which are going to feed the monitored data
of employee access
by comparing the access control
"""

class PushHelper:
    def __init__(self):
        self.con2 = connector.connect(host='localhost',
                                      port='3306',
                                      user='root',
                                      password='##Ajay2000@##',
                                      database='monitoring_database')
        #
        # print(con2)
        query4 = 'create table if not exists monitoring_record(userId int primary key,Dname varchar(20) NOT NULL,' \
                 'contact varchar(10) NOT NULL,email varchar(40) NOT NULL, officeNo int NOT NULL,' \
                 ' Access varchar(3))'

        cur = self.con2.cursor()
        cur.execute(query4)
        print('Created')

"""
Initialing the database and creating required tables
with attributes and pushing some data into the exisiting 
database
"""
helper = DBHelper()
pusher = PushHelper()
helper.insert_data(1, "Ajay Singh Dabi", "7869290946", "ajaydabi20@gmail.com", 2, "dir address", 9, 5, "directors")
helper.insert_data(2, "Sarthak Goyal", "9876545678", "sarthak003@gmail.com", 3, "dir address", 9, 5, "directors")
helper.insert_data(3, "Abhishek Chouhan", "7365583943", "abhishek003@gmail.com", 3, "dir address", 9, 5, "directors")

helper.insert_data(4, "Vineet Kanthaliya", "8594758395", "vineet003@gmail.com", 6, "dir address", 9, 5, "employee")
helper.insert_data(5, "Priyansh Jaiswal", "9495904434", "priyansh003@gmail.com", 7, "dir address", 9, 2, "employee")
helper.insert_data(6, "Pradhumna Mishra", "7689676543", "pradhumna003@gmail.com", 8, "dir address", 12, 5, "employee")
helper.insert_data(7, "Kunal Devda", "9876789876", "kunal003@gmail.com", 12, "dir address", 9, 3, "employee")
helper.insert_data(8, "Rituraj Gaikwad", "8987678987", "rituraj003@gmail.com", 13,  "dir address", 10, 5, "employee")
helper.insert_data(9, "Rohit Bhati", "9878765434", "rohit003@gmail.com", 24,  "dir address", 1, 5, "employee")

helper.insert_access_table(4,"Vineet Kanthaliya",2)
helper.insert_access_table(4,"Vineet Kanthaliya",3)
helper.insert_access_table(4,"Vineet Kanthaliya",4)
helper.insert_access_table(5,"Priyansh Jaiswal",6)
helper.insert_access_table(5,"Priyansh Jaiswal",7)
helper.insert_access_table(5,"Priyansh Jaiswal",3)
helper.insert_access_table(6,"Pradhumna Mishra",5)
helper.insert_access_table(6,"Pradhumna Mishra",6)
helper.insert_access_table(6,"Pradhumna Mishra",8)
helper.insert_access_table(7,"Kunal Devda",8)
helper.insert_access_table(7,"Kunal Devda",7)
helper.insert_access_table(7,"Kunal Devda",12)
helper.insert_access_table(8,"Rituraj Gaikwad",23)
helper.insert_access_table(8,"Rituraj Gaikwad",4)
helper.insert_access_table(8,"Rituraj Gaikwad",24)
helper.insert_access_table(9,"Rohit Bhati",6)
helper.insert_access_table(9,"Rohit Bhati",9)

"""
This method will help us fetch the data from
the existing_database to compare
"""
helper.Pull_Data()










