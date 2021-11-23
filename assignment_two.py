
pin = input("Type your secret pin number: ")
balance = 2000


while True:
    print("Hello! Welcome to our ATM service")
    print(" 1. Balance Checking \n 2. Cash Withdrawal \n 3. Cash Deposition \n 4. Exit")
    print("*******?*******?*")

    try:
        choice = int(input("Please proceed with your choice: "))
        if choice == 1:
            print("\n")
            print("Your account balance is Rs : " + str(balance))
            print("\n")
            next_prompt = input(
                "Would you like to have another ATM transaction?(y/n): ")
            if next_prompt == "n":
                break
            elif next_prompt == "y":
                pass

        elif choice == 2:
            amount = int(input("Insert the amount to be withdrawal: "))
            balance = balance - amount
            print("\n")
            print("You can now collect the cash")
            print("Your balance is" + str(balance))
            print("\n")
            next_prompt = input(
                "Would you like to have another ATM transaction?(y/n): ")
            if next_prompt == "n":
                break
            elif next_prompt == "y":
                pass
        elif choice == 3:
            amount = int(input("Insert the amount to be deposited: "))
            balance = balance + amount
            print("\n")
            print("You can now collect the cash")
            print("Your balance is " + str(balance))
            print("\n")
            next_prompt = input(
                "Would you like to have another ATM transaction?(y/n): ")
            if next_prompt == "n":
                break
            elif next_prompt == "y":
                pass
        elif choice == 4:
            print("We are thankful to you for USING our ATM services!")
            break
    except:
        pass
