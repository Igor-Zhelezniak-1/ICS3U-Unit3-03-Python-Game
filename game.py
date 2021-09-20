#!/usr/bin/env python3

# Created by: Igor
# Created on: Sept 2021
# This is game

import constans


def main():
    # This is game

    # input
    number = int(input("Enter the number between 0-9: "))

    # process
    if number == constans.secret_number:
        print("You guessed correct!")
    else:
        print(
            "You guessed wrong! The number was {0}".format(
                constans.secret_number
            )
        )
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
