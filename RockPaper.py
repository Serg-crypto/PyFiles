import random
options = ['rock','paper','scissors']
print("Rock is 0\t Paper is 1\t scissors is 2 ")
user = input("Select an option between 'Rock', 'Paper' or 'Scissors': \n")
user_option = user.lower()


if user_option not in options:
    print("You have to choose an option")
else:
    rival = random.randint(0,2)
    if rival == 0:
        if user_option == 'rock':
            print("Draw")
        elif user_option == 'paper':
            print("You win!")
        elif user_option == 'scissors':
            print("Game Over!")
    elif rival == 1:
        if user_option == 'rock':
            print("Game over!")
        elif user_option == 'paper':
            print("Draw")
        elif user_option == 'scissors':
            print("You win!")
    elif rival == 2:
        if user_option == 'rock':
            print("You win!")
        elif user_option == 'paper':
            print("Game Over!")
        elif user_option == 'scissors':
            print("Draw!")

