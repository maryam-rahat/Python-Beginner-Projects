# rock paper scissor

import random

exit = False
score = 0
comp = 0

while exit == False:
    options = ['rock', 'paper', 'scissors', 'exit']
    user_input = input('Choose rock, paper, scissors or exit: ').lower()
    computer_input = random.choice(options)

    if user_input == 'exit':
        print('Game ended')
        print('Your score', score)
        print("Computer's Score", comp)
        exit = True

    if user_input == 'rock':

        if computer_input == 'rock':
            print('rock')
            print('rock')
            print("It's a tie")
        elif computer_input == 'paper':
            print('rock')
            print('paper')
            print("You lose")
            comp += 1
        elif computer_input == 'scissor':
            print('rock')
            print('scissor')
            print("You win")
            score +=1

    elif user_input == 'paper':

        if computer_input == "paper":
            print("paper")
            print('paper')
            print("It's a tie")
        elif computer_input == 'rock':
            print('paper')
            print('rock')
            print('You win')
            score +=1
        elif computer_input == 'scissor':
            print('paper')
            print('scissor')
            print('You lose')
            comp +=1

    elif user_input == 'scissors':

        if computer_input == 'rock':
            print('scissors')
            print('rock')
            print("You lose")
            comp +=1
        elif computer_input == 'scissors':
            print('scissors')
            print('scissors')
            print("It's a tie")
        elif computer_input == 'paper':
            print('scissors')
            print('paper')
            print('You win')
            score +=1

    elif user_input != options:
        print("")