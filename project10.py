# import random
# def funtion to roll the dice
# dictionary for the images of dice
# while loop

import random

def roll_dice():
    dice_art = {
        1: [" ------- ",
            "|       |",
            "|   O   |",
            "|       |",
            " ------- "],
        2: [" ------- ",
            "| O     |",
            "|       |",
            "|     O |",
            " ------- "],
        3: [" ------- ",
            "| O     |",
            "|   O   |",
            "|     O |",
            " ------- "],
        4: [" ------- ",
            "| O   O |",
            "|       |",
            "| O   O |",
            " ------- "],
        5: [" ------- ",
            "| O   O |",
            "|   O   |",
            "| O   O |",
            " ------- "],
        6: [" ------- ",
            "| O   O |",
            "| O   O |",
            "| O   O |",
            " ------- "],
    }

    roll = input("Roll the dice? (y/n): ")

    while roll.lower() == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("DICE ROLLED: {} and {}".format(dice1, dice2))
        print("\n".join(dice_art[dice1]))
        print("\n".join(dice_art[dice2]))

        roll = input("Roll again (y/n): ")

roll_dice()