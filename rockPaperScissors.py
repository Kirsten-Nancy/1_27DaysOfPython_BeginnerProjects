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
choices = [rock, paper, scissors]

validInput = ['0','1','2']

while True:
    # To account for any type of input, str, int...
    userInput = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for scissors\n")
    if userInput not in validInput:
        print('Not a valid input, Please follow the above instructions.\n')
        continue
    else: 
        playerMove = int(userInput)      
        print(choices[playerMove])
        break

computerMove = random.randint(0,2)
print('Computer chose:')
print(choices[computerMove])


# and is executed before or
if computerMove == 0 and playerMove == 2 or computerMove == 2 and playerMove == 1 or computerMove == 1 and playerMove == 0:
    print('You lose!')
elif playerMove == 0 and computerMove == 2 or playerMove == 2 and computerMove == 1 or playerMove == 1 and computerMove == 0:
    print('You Win!')
elif computerMove == playerMove:
    print('It\'s a tie')





 
