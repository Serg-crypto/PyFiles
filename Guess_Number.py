import random
import pyfiglet
BJ = "Guess my number!"
ASCII_art_1 = pyfiglet.figlet_format(BJ)
print(ASCII_art_1)




def game():
    attempts = 0
    numberRival = random.randint(1, 100)
    user_mode = input("Select the level: Easy or Hard\n ").lower()

    if user_mode == "easy":
        user_number = int(input("Guess the number I'm thinking:\n"))
        attempts = 10
        if user_number == numberRival:
            print("---------------------------------------------------------------------------------------------------")
            print("You win!!!!")
            print(f"Secret number: {numberRival}\tyour number: {user_number}")
        elif user_number != numberRival:
            print("Nope!")
            print("---------------------------------------------------------------------------------------------------")

            while user_number != numberRival:
                user_number = int(input("Guess the number I'm thinking:\n"))
                attempts = attempts - 1
                if attempts == 0:
                    if user_number == numberRival:
                        print("---------------------------------------------------------------------------------------------------")
                        print("\t\t\t\t\tYou win!!!!")
                        print(f"Secret number: {numberRival}\tyour number: {user_number}")
                    else:
                        print(f"Game Over!\t\t\t\t\t the number is {numberRival}")
                        break
                elif user_number == numberRival:
                    print("---------------------------------------------------------------------------------------------------")
                    print("\t\t\t\t\tYou win!!!!")

                    print(f"Secret number: {numberRival}\tyour number: {user_number}")
                elif user_number > numberRival:
                    print("---------------------------------------------------------------------------------------------------")
                    print(f"Your number is higher than the secret number \n Attempts left: {attempts}")
                elif user_number < numberRival:
                    print("---------------------------------------------------------------------------------------------------")
                    print(f"Your number is lower than the secret number \n Attempts left: {attempts}")



    elif user_mode == "hard":
        user_number = int(input("Guess the number I'm thinking:\n"))
        attempts = 5
        if user_number == numberRival:
            print("---------------------------------------------------------------------------------------------------")
            print("You win!!!!")
            print(f"Secret number: {numberRival}\tyour number: {user_number}")
        elif user_number != numberRival:
            print("Nope!")
            print("---------------------------------------------------------------------------------------------------")
            while user_number != numberRival:
                user_number = int(input("Guess the number I'm thinking:\n"))
                attempts = attempts - 1
                if attempts == 0:
                    if user_number == numberRival:
                        print("---------------------------------------------------------------------------------------------------")
                        print("\t\t\t\t\tYou win!!!!")
                        print(f"Secret number: {numberRival}\tyour number: {user_number}")
                    else:
                        print(f"Game Over!\t\t\t\t\t the number is {numberRival}")
                        break
                elif user_number == numberRival:
                    print("---------------------------------------------------------------------------------------------------")
                    print("\t\t\t\t\tYou win!!!!")
                    print(f"Secret number: {numberRival}\tyour number: {user_number}")

                elif user_number > numberRival:
                    print(
                        "---------------------------------------------------------------------------------------------------")
                    print(f"Your number is higher than the secret number \n Attempts left: {attempts}")
                elif user_number < numberRival:
                    print(
                        "---------------------------------------------------------------------------------------------------")
                    print(f"Your number is lower than the secret number \n Attempts left: {attempts}")

    else:
        print("You have to select an option!")
        game()



start = input("Press 'Go' to start the game: ").lower()
while start != "go":
    start = input("Press 'Go' to start the game: ").lower()

if start == "go":
    game()


again = input("Do you want to play again? Yes or No? ").lower()
if again == "yes":
    game()
else:
    print("Ok Bye!")