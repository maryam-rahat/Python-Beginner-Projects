# random password generator
# ask them (yes/no)
# if yes : ask for the password length
# generate the password
# print the password
# if no: exit

import sys
import random
import string

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def yes():
    length = int(input("What would you like to be the length of your password: "))

    random.shuffle(characters)

    password = []

    for i in range(length):  # this is where it sees the length
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)

def no():
    sys.exit("Thank you so much.")

def main():
    print("This is a random password generator.")
    print('')

    ask = input("Do you need my assistance? (yes/no): ")

    if ask.lower() == 'yes':
        yes()

    elif ask.lower() == 'no':
        no()

    else:
        sys.exit("Invalid Request.")


if __name__ == "__main__":
    main()