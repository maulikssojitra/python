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

list = [rock, paper, scissors]
you_Choose = int(input("Take your Turn : "))
print(f"your choice is {list[you_Choose]}")

computer_choose = random.randint(0, 2)
print(f"computer choice is {computer_choose} \n {list[computer_choose]}")

if you_Choose < 0 or you_Choose > 2:
    print("Invalid choice! Please choose a number between 1 and 3.")
else:
    if you_Choose == computer_choose:
        print("It's a draw!")
    elif (you_Choose == 0 and computer_choose == 2) or \
         (you_Choose == 1 and computer_choose == 0) or \
         (you_Choose == 2 and computer_choose == 1):
        print("Congratulations, you won!")
    else:
        print("Sorry, you lost this time. :(")
