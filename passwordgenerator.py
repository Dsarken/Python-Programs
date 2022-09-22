import string
import random


characters = string.ascii_letters + \
    string.digits + '!@#$%^&*()'


def random_password(length):
    return ''.join(random.choice(characters) for i in range(length))


def main():
    choice = input("Do you want to generate a password?(Yes/No) ")
    if choice == 'Yes':
        password_length = int(input("Enter length of password to generate: "))
        print(random_password(password_length))
    elif choice == 'No':
        quit()
    else:
        print("Invalid response please enter Yes or No")
        main()


if __name__ == "__main__":
    main()
