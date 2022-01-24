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

#Write your code bel2ow this line 👇

lists = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n => "))

player_choice = lists[player]
computer_choice = random.choice(lists)



#draw-------------------------------------------------------------------------------------------------
if (player_choice == rock) and (computer_choice == rock ):
  print(f"draw {player_choice}{computer_choice}")
elif (player_choice == scissors) and (computer_choice == scissors ):
  print(f"draw {player_choice}{computer_choice}")
elif (player_choice == paper) and (computer_choice == paper ):
  print(f"draw {player_choice}{computer_choice}")
# loser---------------------------------------------------------------------------------------------------------
elif (player_choice == scissors) and (computer_choice == rock ):
  print(f"computer wins bich {player_choice}{computer_choice}")
elif (player_choice == paper) and (computer_choice == rock ):
  print(f"computer wins bich {player_choice}{computer_choice}")

elif (player_choice == rock) and (computer_choice == paper ):
  print(f"computer wins bich {player_choice}{computer_choice}")
# winner ---------------------------------------------------------------------------------------
elif (computer_choice == scissors) and (player_choice == rock ):
  print(f"you wins bich {player_choice}{computer_choice}")

elif (computer_choice == paper) and (player_choice == rock ):
  print(f"you wins bich {player_choice}{computer_choice}")

elif (computer_choice == rock) and (player_choice == paper ):
  print(f"you wins bich {player_choice}{computer_choice}")
