def main_menu():
    print("----Welcome! to employee leave system.----")
    print("1. Register employee")
    print("2. Apply leave")
    print("3. View leaves")
    print("4. Exit")

while True:
    main_menu()
    opti = input("Enter your option: ")
    if opti == "1":
        print("Register employee")
    elif opti == "2":
        print("Apply leave")
    elif opti == "3":
        print("View leaves")
    elif opti == "4":
        print("Good bye.")
    break
else:
        print("Invalid choice !")