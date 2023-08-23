import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          ________)
         ________)
---.___________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_score = 0
computer_score = 0


def game():
    print("This is a best of 5 game! First to score 3 points will win.")
    global user_score, computer_score

    def score_track():
        print(" 🙍‍♂️   SCORE     💻")
        print(f"User   {user_score}:{computer_score}   Computer")

    while user_score < 3 and computer_score < 3:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
        if 0 <= user_choice <= 2:
            print(game_images[user_choice])

            computer_choice = random.randint(0, 2)
            print("Computer chose:")
            print(game_images[computer_choice])

            if user_choice == 0 and computer_choice == 2:
                # user wins
                user_score += 1
                score_track()
            elif computer_choice == 0 and user_choice == 2:
                # computer wins
                computer_score += 1
                score_track()
            elif computer_choice > user_choice:
                # computer wins
                computer_score += 1
                score_track()
            elif user_choice > computer_choice:
                # user wins
                user_score += 1
                score_track()
            elif computer_choice == user_choice:
                # draw
                score_track()
        else:
            print("You typed an invalid number! Try again.")

    if user_score > computer_score:
        print("Congrats! You win. 🥳🥳")
    elif computer_score > user_score:
        print("Computer wins! Better luck next time. 😄😄\n")
    play_again = input("Do you want to play again? Type 'y' for Yes and 'n' for No: ").lower()
    if play_again == "y":
        user_score = 0
        computer_score = 0
        print("\n")
        game()
    elif play_again == "n":
        print("Bye!")
    else:
        print("Invalid choice! Please rerun this program to play again.")


game()
