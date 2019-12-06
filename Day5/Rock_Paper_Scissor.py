
import random as r
user_input = int(input("1. Rock\n2. Paper\n3. Scissor \n Enter any(1/2/3)"))
com_input = r.randint(1, 3)
choices = ['Rock', 'Paper', 'Scissor']
print("You Selected ", choices[user_input-1], "Computer selected ", choices[com_input-1])
if user_input == com_input:
    print("Game Drawn")
elif user_input == 1 and com_input == 2:
    print("Computer Wins")
elif user_input == 1 and com_input == 3:
    print("User Wins")
elif user_input == 2 and com_input == 1:
    print("User Wins")
elif user_input == 2 and com_input == 3:
    print("Computer Wins")
elif user_input == 3 and com_input == 1:
    print("Computer Wins")
elif user_input == 3 and com_input == 2:
    print("User Wins")
else:
    print("Invalid Input")
