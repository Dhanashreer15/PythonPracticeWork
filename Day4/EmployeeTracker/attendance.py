from config import get_connection
from mysql.connector import Error
from datetime import datetime

class Employee:
    def add_employee(self,name,dept):
        try:
            conn=get_connection()
            cursor=conn.cursor()
            cursor.execute("insert into employee(name,dept) values(%s,%s)",(name,dept))
            conn.commit()
            print(f"Employee {name} added.")
        except Error as e:
            print("Database error:",e)
        finally:
            cursor.close()
            conn.close()

    def check_in(self,employee_id):
        try:
            conn=get_connection()
            cursor=conn.cursor()
            cursor.execute("select * from attendance where employee_id=%s and check_out is null",(employee_id,))
            if cursor.fetchone():
                print("Already checked in.")
                return
            cursor.execute("insert into attendance(employee_id,check_in) values(%s,%s)",(employee_id,datetime.now()))
            conn.commit()
            print("Check-in successful.")
        except Error as e:
            print("Error during check-in:",e)
        finally:
            cursor.close()
            conn.close()

    def check_out(self,employee_id):
        try:
            conn=get_connection()
            cursor=conn.cursor()
            cursor.execute("select attendance_id,check_in from attendance where employee_id=%s and check_out is null",(employee_id,))
            record=cursor.fetchone()
            if not record:
                print("No active check-in found.")
                return
            attendance_id,check_in_time=record
            check_out_time=datetime.now()
            total_hours=(check_out_time-check_in_time).total_seconds()/3600
            cursor.execute("update attendance set check_out=%s,total_hours=%s where attendance_id=%s",(check_out_time,total_hours,attendance_id))
            conn.commit()
            print("Check-out successful.")
        except Error as e:
            print("Error during check-out:",e)
        finally:
            cursor.close()
            conn.close()

    def show_attendance(self,employee_id=None):
        try:
            conn=get_connection()
            cursor=conn.cursor()
            if employee_id:
                cursor.execute("select * from attendance where employee_id=%s",(employee_id,))
            else:
                cursor.execute("select * from attendance")
            for row in cursor.fetchall():
                print(row)
        except Error as e:
            print("Error fetching attendance:",e)
        finally:
            cursor.close()
            conn.close()

    def show_pending_checkouts(self):
        try:
            conn=get_connection()
            cursor=conn.cursor()
            cursor.execute("select * from attendance where check_out is null")
            for row in cursor.fetchall():
                print(row)
        except Error as e:
            print("Error fetching pending check-outs:",e)
        finally:
            cursor.close()
            conn.close()
