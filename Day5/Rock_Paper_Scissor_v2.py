# Circular Checking Algorithm
import random as r
user_wins = com_wins = 0
print('1. Rock\n2. Paper\n3. Scissor \n ')
choices = ['Rock', 'Paper', 'Scissor']
for i in range(3):
    user_input = int(input("Enter any(1/2/3)"))
    com_input = r.randint(1, 3)
    print("You Selected ", choices[user_input-1], "Computer selected ", choices[com_input-1])
    decision = (user_input - com_input) % 3
    if decision == 0:
        print("Draw")
    elif decision == 2:
        print("Computer Wins this set")
        com_wins += 1
    elif decision == 1:
        print("User Wins this set")
        user_wins += 1
    else:
        print("Invalid input")
if com_wins > user_wins:
    print("\nComputer Wins Best of three")
elif user_wins > com_wins:
    print("\nUser Wins the best of three")
else:
    print("\nGame Drawn in best of three")