""""rock wins against scissors,
    scissors wins against paper,
    paper wins against rock"""

import random

print("Welcome to Rock, Paper, Scissors Game!")

user_choice = int(input("Enter your choice (0 for rock, 1 for paper, 2 for scissors):"))
computer_choice = random.randint(0, 2)
print(f"The computer chose: {computer_choice}")

if user_choice >= 3:
    print("Invalid choice. Please choose from 0, 1, or 2.")

if user_choice == computer_choice:
    print("Bruh, it's a tie.")
elif user_choice == 0 and computer_choice == 2:
    print("Yayy! you win!")
elif user_choice == 2 and computer_choice == 0:
    print("Oh no! you lose.")
elif user_choice > computer_choice:
    print("Yayy! you win!")
elif computer_choice > user_choice:
    print("Oh no! you lose.")

    
