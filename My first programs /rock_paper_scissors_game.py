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
list_of_options = [rock, paper, scissors]
user_choice = int(input("Choose 0 for rock, 1 for paper or 2 for scissors: "))
print(f"You chose: \n"
      f"{list_of_options[user_choice]}")

computer_choice = random.randint(0, 2)
print(f"Computer chose: {list_of_options[computer_choice]}")
if user_choice == computer_choice:
    print("It\'s a draw!")
elif computer_choice == 2 and user_choice == 0:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")


