import random


def password_generator(choice):
    random_password = ''
    new_set = """@#$%^&*1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}[]()/\\'"`~,;:.<>"""
    if choice == 1:
        for i in range(0, 4):
            chosen_letter = random.choice(new_set)
            random_password += chosen_letter
    if choice == 2:
        for i in range(0, 8):
            chosen_letter = random.choice(new_set)
            random_password += chosen_letter
    if choice == 3:
        for i in range(0, 16):
            chosen_letter = random.choice(new_set)
            random_password += chosen_letter
    if choice == 4:
        for i in range(0, 32):
            chosen_letter = random.choice(new_set)
            random_password += chosen_letter
    if choice == 5:
        for i in range(0, 48):
            chosen_letter = random.choice(new_set)
            random_password += chosen_letter
    if choice == 6:
        for i in range(0, 64):
            chosen_letter = random.choice(new_set)
            random_password += chosen_letter
    if choice == 7:
        for i in range(0, 128):
            chosen_letter = random.choice(new_set)
            random_password += chosen_letter
    print(f"This is your generated password: {random_password}")
    print(len(random_password))


def main():
    print("This is a Password generator")
    print("You have a choice of several lengths to make your password:")
    print("1. 4 characters long")
    print("2. 8 characters long")
    print("3. 16 characters long")
    print("4. 32 characters long")
    print("5. 48 characters long")
    print("6. 64 characters long")
    print("7. 128 characters long")
    choice = int(input("Choose a password length: "))
    password_generator(choice)


if __name__ == '__main__':
    main()
