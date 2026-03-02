# main program 

print("***WELCOME*** \n***EXPENSE CALCULATOR***\n")


def menu():
    print("Choose the number from MENU to perform the desired action. \n")
    print("1) Add Receipt\n2) Display\n3) Update\n4) Exit\n ")
    choice = input("Enter your choice: ")

    while choice=="":
        print("\nChoose the number from MENU to perform the desired action. \n")
        print("1) Add Receipt\n2) Display\n3) Update\n4) Exit ")
        choice = input("Enter your choice: ")


menu() 