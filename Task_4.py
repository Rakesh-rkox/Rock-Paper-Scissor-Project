#import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# random_float = random.uniform(1, 10)
# print(random_float)

# Heads or Tails Project:
# Heads_or_Tails = random.randint(1, 10)
# if Heads_or_Tails <= 5:
#     print("Heads")
# else:
#     print("Tails")

#Bank Roulette Project:
# friends = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
# random_choice = random.randint(0, len(friends) - 1)
# print(random.choice(friends) + " is going to buy the meal today!")
# print(friends[random_choice] + " is going to buy the meal today!")

#Rock Paper Scissors Project:

import random
# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice>=0 and user_choice<=2:
    print(game_images[int(user_choice)])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose: {computer_choice}")

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw!")
