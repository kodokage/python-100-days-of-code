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

#Write your code below this line 👇
user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
import random
computer = random.randint(1,3)

rps = [rock, paper, scissors]

print('User = ', rps[int(user_input)])

print('Computer = ', rps[computer - 1])

if  int(user_input) == 1 and ((computer - 1 ) == 0 ):
  print("You win")
  
elif  int(user_input) == 0 and ((computer - 1 ) == 2 ):
  print("You Win")

elif  int(user_input) == 2 and ((computer - 1 ) == 1 ):
  print("You Win")

elif  int(user_input) == 0 and ((computer - 1 ) == 1 ):
  print("You Loose")

elif  int(user_input) == 1 and ((computer - 1 ) == 2 ):
  print("You Loose")

elif  int(user_input) == 2 and ((computer - 1 ) == 0 ):
  print("You Loose")

else:
  print("This is a draw Draw")
