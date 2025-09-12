from attendance import Employee

def main():
    emp=Employee()

    while True:
        print("\n--- Employee Attendance Menu ---")
        print("1. Add Employee")
        print("2. Check In")
        print("3. Check Out")
        print("4. Show Attendance")
        print("5. Show Pending Check-Outs")
        print("6. Exit")

        choice=input("Enter your choice: ")

        if choice=="1":
            name=input("Enter employee name: ")
            dept=input("Enter department: ")
            emp.add_employee(name,dept)

        elif choice=="2":
            emp_id=input("Enter employee ID: ")
            emp.check_in(emp_id)

        elif choice=="3":
            emp_id=input("Enter employee ID: ")
            emp.check_out(emp_id)

        elif choice=="4":
            emp_id=input("Enter employee ID (or press Enter to show all): ")
            if emp_id.strip()=="":
                emp.show_attendance()
            else:
                emp.show_attendance(emp_id)

        elif choice=="5":
            emp.show_pending_checkouts()

        elif choice=="6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__=="__main__":
    main()
