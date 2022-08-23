import random
import sys

"""This program generates a random name based off of a first name and a surname"""
print("Enter '0' to quit the program or '1' to use the generator")
choice = int(input())


def main():
    if choice == 0:
        exit()


if choice == 1:
    anime_first_name = (
        'Masashi',
        'Michi',
        'Natsu',
        'Noburu',
        'Nori',
        'Osamu',
        'Raiden',
        'Michiaki',
        'Yasu',
        'Michio',
        'Tatsuya'
        'Mikio',
        'Toshiro',
        'Levi',
        'Yoshimoto')

anime_last_name = ('Sato'
                   'Suzuki',
                   'Takahashi',
                   'Tanaka',
                   'Watanabe',
                   'Ito',
                   'Yamamoto',
                   'Nakamura',
                   'Kobayashi',
                   'Kato',
                   'Yoshida',
                   'Yamada',
                   'Sasaki',
                   'Ackermann',
                   'Imagawa')

while True:
    first_name = random.choice(anime_first_name)
    last_name = random.choice(anime_last_name)
    print("\n\n")
    print("{} {}".format(first_name, last_name))
    print('\n\n')
    try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
    if try_again.lower() == "n":
        break
input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()
