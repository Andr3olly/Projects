import random

print("*** WELCOME TO THE PASSWORD GENERATOR ***")
print("- made by Andr3olly -")

def password_generator():
    lowercase = "qwertyuiopasdfghjklzxcvbnm"
    uppercase = "QWERTYUIOPASDFGHJKLZXCVBNM"
    numbers = "0123456789"
    simbols = "!£$%&*@#"
    all = lowercase + uppercase + numbers + simbols

    length = int(input("Enter the length of the password -> "))

    password = "".join(random.sample(all , length))
    print(password)

    repeat = input("Do you want to generate another password? y/n -> ")

    if repeat == "y" or repeat == "Y":
        return password_generator()
    else:
        quit()

password_generator()