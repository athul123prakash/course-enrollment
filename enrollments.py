

import mysql.connector
con=mysql.connector.connect(user='root',password='tiger',host='localhost',database='course_enrollment')


class Student():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(user='root',password='tiger',host='localhost',database='course_enrollment')
            print("connected")
        except:
            print("unable to connect")

    def enroll(self,enrollment_id,student_name,course_name,duration_months,enrollment_date,fee,status):
        try:
            cursor=self.con.cursor()
            query="insert into enrollments(enrollment_id,student_name,course_name,duration_months,enrollment_date,fee,status)values(%s,%s,%s,%s,%s,%s,%s)"
            data=(enrollment_id,student_name,course_name,duration_months,enrollment_date,fee,status)
            cursor.execute(query,data)
            self.con.commit()
            print("enrolled")
        except:
            print("unable to enroll")

    def view(self):
        try:
            cursor=self.con.cursor()
            query="select * from enrollments where status=%s order by fee desc"

            cursor.execute(query,)
            records=cursor.fetchall()
            if records:
                for row in records:
                    print(row)
            else:
                print("no records")
        except:
            print("failed")

    def search(self,id):
        try:
            cursor=self.con.cursor()
            query="select * from enrollments where enrollment_id=%s"
            data = (id,)
            cursor.execute(query, data)
            records = cursor.fetchone()
            if records:
                print(records)
            else:
                print("no records")

        except:
            print("failed")

    def update(self,enrollment_id,status,fee):
        try:
            cursor=self.con.cursor()
            query="update enrollments set status=%s, fee=%s where enrollment_id=%s"
            data=(status,fee,enrollment_id)
            cursor.execute(query,data)
            self.con.commit()
            if cursor.rowcount>0:
                print("updated")
            else:
                print("no records")
        except:
            print("failed")

    def delete(self,enrollment_id):
        try:
            cursor=self.con.cursor()
            query="Select count(*) ,sum(fee) from enrollments group by status"
            data=(enrollment_id,)
            cursor.execute(query,data)
            self.con.commit()
            if cursor.rowcount>0:
                print("delete success")
            else:
                print("no records")
        except:
            print("failed")

s=Student()

while(1):
    print('1.enroll student')
    print('2.view all enrollments')
    print('3.search enrollment')
    print('4.update enrollment status')
    print('5.delete enrollment')
    print('6.exit')

    ch=int(input('enter your choice:'))
    if ch==1:
        i=int(input('Enter your enrollment_id:'))
        n=input('Enter your student_name:')
        c=input('Enter your course_name:')
        d=int(input('Enter your duration_months:'))
        e=int(input('Enter your enrollment_date:'))
        f=int(input('Enter your fee:'))
        s=input('Enter your status:')
        s.enroll(i,n,c,d,e,f,s)

    elif ch==2:

        s.view()
    elif ch==3:
        i=int(input('Enter your id:'))
        s.search(i)
    elif ch==4:
        i=int(input('Enter your id:'))
        s=input('Enter your status:')
        f=int(input('Enter your fee:'))
        s.update(i,s,f)
    elif ch==5:
        i=int(input('Enter your id:'))
        s.delete(i)

    else:
        exit()








            







