valid = False
password = ""
while not valid:
    password = input("Create a password: ")
    if(len(password) < 6):
        print("Invalid password, password must be six or more characters in length")
    elif not any(char.isdigit() for char in password):
        print("Invalid password, password must have atleast one number")
    elif not any(not c.isalnum() for c in password):
        print("Invalid password, password must have atleast one special character")
    else:
        valid = True


number_one, number_two = "", ""

while (not number_one and not number_two):
    try:
        number_one = int(input("Enter a number: "))
        number_two = int(input("Enter another number: "))

        result = number_one + number_two

        attempts = 3

        while attempts > 0:
            confirm_pass = input("Enter your password to view the result: ")
            if confirm_pass != password:
                if attempts == 1: 
                    print("You have exhausted the number of trials given to you")
                attempts = attempts - 1
                print("Wrong password " + str(attempts) + " attempts left.")
            else:
                print("The result is: " + str(result))
                break

    except:
        pass
