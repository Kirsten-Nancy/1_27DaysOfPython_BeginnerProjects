import random, gameData, art, os

listOfData = gameData.data
# Initial list of people
gameList = []
# Randomly choose an a person from the data, 2 then add to the gameList

person1 = random.choice(listOfData)
person2 = random.choice(listOfData)
gameList.append(person1)
# To always ensure the the two dictionaries chosen are not duplicates
while person2 == person1:
    person2 = random.choice(listOfData)
gameList.append(person2)

# print(gameList)

def moreFollowers(userOption, option2):
    """To determine which of the two people in current game list has more followers"""
    if userOption['follower_count'] > option2['follower_count']:
        # print(f"{userOption['name']} has more followers than {option2['name']}.")
        return True
    else:
        # print(f"{option2['name']} has more followers than {userOption['name']}.")
        return False

def checkAnswer(answer):
    """Check whether the person the player chose has more followers or not, 
        to determine if the game continues or not."""
    if answer == 'A':
        answer = gameList[0]
        return moreFollowers(answer,gameList[1])
    elif answer == 'B':
        answer = gameList[1]
        return moreFollowers(answer, gameList[0])


def playGame():
    score = 0
    while True:
        # At this point we already know A = person1, B = person2, so definitely we know their scores
        print(f"Compare A: {gameList[0]['name']}, {gameList[0]['description']} from {gameList[0]['country']}")
        print(art.vs)
        print(f"Against B: {gameList[1]['name']}, {gameList[1]['description']} from {gameList[1]['country']}")

        playerChoice = input("Who has more followers 'A' or 'B': ").upper()

        continueGame = checkAnswer(playerChoice)

        os.system('cls')
        print(art.logo)
        
        # If the player chose the right answer, the game continues
        if continueGame:
            del(gameList[0])
            gameList.append(random.choice(listOfData))
            # print(gameList)
            score += 1
            print(f"You're right. Your current score: {score}")
        else:
            print(f"You got it wrong. Your final score {score}")
            break
        

print(art.logo)  
playGame()
