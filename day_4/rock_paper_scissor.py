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
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


# player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

# # put choices in a list
# choices = [rock, paper, scissors]

# # Define the players choice
# player = choices[int(player_choice)]


# # Create computer choice at random
# computer = random.choice(choices)

# # Compare player and computer choices to determine winner
# if player == rock and computer == rock:
#     print('Computer chose rock, its a draw.')
# elif player == rock and computer == paper:
#     print('Computer chose paper, paper covers rock. You lose!')
# elif player == rock and computer == scissors:
#     print('Computer chose scissors, rock smashes scissors. You WIN!')

# if player == paper and computer == paper:
#     print('Computer chose paper, its a draw.')
# elif player == paper and computer == rock:
#     print('Computer chose rock, paper covers rock. You WIN!')
# elif player == paper and computer == scissors:
#     print('Computer chose scissors, scissors cut paper. You lose!')

# if player == scissors and computer == scissors:
#     print('Computer chose scissors, its a draw.')
# elif player == scissors and computer == paper:
#     print('Computer chose paper, scissors cut paper. You WIN!')
# elif player == scissors and computer == rock:
#     print('Computer chose rock, rock smashes scissors. You lose!')


# print(computer)

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if user_choice >= 3:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose: ")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
