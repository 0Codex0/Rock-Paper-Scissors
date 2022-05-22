print("Welcome To Rock Paper Scissors")

print("Rock is 0")
print("Paper is 1")
print("Scissors is 2")
print("Press ENTER after you enter your choice. there is 3 rounds")

import time
time.sleep(3)

print()

import random

user_points = 0
computer_points = 1

for i in range(3):

  Player = ["rock", "paper", "scissors"]
  
  player_choice = int(input("what will you play?\n"))
      
  R_P_S = ["rock", "paper", "scissors"]

  computer_choice = random.randint(0, 2)

  print(f'User choice: {Player[player_choice]}')
  print(f'Computer choice: {R_P_S[computer_choice]}')
  
  if(Player[player_choice]==R_P_S[computer_choice]):
    print("It's a Tie")
    user_points += 1
    computer_points += +1
  if(Player[player_choice]==Player[0] and R_P_S[computer_choice]==R_P_S[1]):
    computer_choice += 1
    print("the computer won")
  if(Player[player_choice]==Player[1] and R_P_S[computer_choice]==R_P_S[0]):
    user_points += 1
    print("Player won")
print()
print()
print("Player points:" + str(user_points))
print("Computer points:" + str(computer_points))

if user_points < computer_points:
  print("You Lose")
elif user_points>computer_points:
  print("You Win")
elif user_points==computer_points:
  print("Tie")
