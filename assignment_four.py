
name = input("Enter your name: ")
pin = input("Type your secret pin number: ")


balance = 10000

f = open("transactions.txt", "w+")


def check_balance():
    record("cb", str(balance))
    print("\n")
    print("Your account balance is Rs : " + str(balance))
    print("\n")


def deposit_cash():
    global balance
    global record
    try:
        amount = int(input("Insert the amount to be deposited: "))
        record("d", str(amount))
        balance = balance + amount
        print("\n")
        print("You can now collect the cash")
        print("Your balance is " + str(balance))
        print("\n")
    except:
        print("Invalid")


def withdraw_cash():
    global balance
    global record
    try:
        amount = int(input("Insert the amount to be withdrawal: "))
        if(balance > amount):
            balance = balance - amount
            record("w", str(amount))
            print("\n")
            print("You can now collect the cash")
            print("Your balance is" + str(balance))
            print("\n")
        else:
            print("Insufficient funds")
    except:
        print("Invalid")


def user_is_valid():
    return len(pin) == 4 and len(name) > 1


f.write("name," + name + "\n")
f.write("pin," + pin + " \n")
f.write("bal," + str(balance) + " \n")


def record(type,  amount):
    f.write(type + "," + amount + "\n")
    f.write("bal," + str(balance) + "\n")


def main():
    while True:
        if not user_is_valid():
            print("Invalid user")
            f.close()
            break

        print("Hello! Welcome to our ATM service")
        print(" 1. Balance Checking \n 2. Cash Withdrawal \n 3. Cash Deposition \n 4. Exit")
        print("*******?*******?*")

        try:
            choice = int(input("Please proceed with your choice: "))
            if choice == 1:
                check_balance()
                next_prompt = input(
                    "Would you like to have another ATM transaction?(y/n): ")
                if next_prompt == "n":
                    f.close()
                    break
                elif next_prompt == "y":
                    pass

            elif choice == 2:
                withdraw_cash()
                next_prompt = input(
                    "Would you like to have another ATM transaction?(y/n): ")
                if next_prompt == "n":
                    f.close()
                    break
                elif next_prompt == "y":
                    pass
            elif choice == 3:
                deposit_cash()
                next_prompt = input(
                    "Would you like to have another ATM transaction?(y/n): ")
                if next_prompt == "n":
                    f.close()
                    break
                elif next_prompt == "y":
                    pass
            elif choice == 4:
                f.close()
                print("We are thankful to you for USING our ATM services!")
                break
        except:
            pass


main()


class User():
    def __init__(self, name, pin, bal):
        self.name = name
        self.pin = pin
        self.bal = bal

    def __str__(self):
        return "user: " + self.name + " , bal: " + self.bal


while True:
    records = open("transactions.txt", "r")
    contents = records.read().split("\n")

    u_name = ""
    u_pin = ""
    u_bal = ""

    for content in contents:
        if("name" in content):
            try:
                u_name = (content.split(",")[1])
            except:
                continue
        elif("pin" in content):
            try:
                u_pin = (content.split(",")[1])
            except:
                continue
        elif("bal" in content):
            try:
                u_bal = (content.split(",")[1])
            except:
                continue

    user = User(u_name, u_pin, u_bal)
    confirm_name = input("Enter username: ")
    confirm_pin = input("Enter your pin: ")
    try:
        if(confirm_name in user.name and int(user.pin) == int(confirm_pin)):
            main()
        else:
            print("Invalid credentials")
            break
    except:
        pass
