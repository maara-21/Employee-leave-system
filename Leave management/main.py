employees = []
leaves = []
def main_menu():
    print("----Welcome! to employee leave system.----")
    print("1. Register employee")
    print("2. Apply leave")
    print("3. View leaves")
    print("4. Exit")
def employee_regist():
    name = input("Enter employee name: ")
    employee = {"name":name, "Leave bal":20} #Leave days are default
    employees.append(employee)
    print("Employee registered successfully!")
def view_emp():
    if not employees():
        print("Employee not found !")
        return
    for emp in employees:
        print("Name:",name,emp["name"]," | Leave balance:",emp["Leave bal"])

while True:
    main_menu()
    opti = input("Enter your option: ")
    if opti == "1":
        employee_regist()
    elif opti == "2":
        print("Apply leave")
    elif opti == "3":
        view_emp()
    elif opti == "4":
        print("Good bye.")
    break
else:
        print("Invalid choice !")