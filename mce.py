print("***WELCOME*** \n***EXPENSE CALCULATOR***\n")


def addReceipt():
    print("Enter the Date, ShopName, Amount: \n")
    purchase_Date = input("Enter the Date of Purchase: \n")
    shop_Name = input("Enter the Shop Name: \n")
    purchase_Amount = float(input("Enter the Purchase Amount: \n"))

    print(f"Purchase Date: {purchase_Date}, Shop Name: {shop_Name}, Amount: {purchase_Amount} € ")



def display():
    print("The results: ")


def update():
    print("Make the changes here!") 

def exit():
    print("Thanks for using!")

def main():
    print("Choose the number from MENU to perform the desired action. \n")
    print("1) Add Receipt\n2) Display\n3) Update\n4) Exit\n ")
    choice = input("Enter your choice: ")

    while choice=="":
        print("\nChoose the number from MENU to perform the desired action. \n")
        print("1) Add Receipt\n2) Display\n3) Update\n4) Exit ")
        choice = input("Enter your choice: ")

    match choice:

        case "1":
            addReceipt()
        case "2":
            display()
        case "3":
            update()
        case "4":
            exit()
        case _:
            print("Invalid Choice!")


main()