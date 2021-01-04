import random, art

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def calculateScore(alist):
    score = sum(alist)
    # for card in alist:
    #     score += card

    if score == 21 and len(alist) == 2:
        return sum(alist)
        
    if 11 in alist and sum(alist) > 21:
        alist.remove(11)
        alist.append(1)

    return sum(alist)

def dealGame():
    print(f"Your final hand: {player_deck}, current score: {player_score}")
    print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")


    if player_score > 21:
        print("You went over. You lose")
        return 

    if player_score > dealer_score:
        if player_score <= 21:
            print("You win")
        else:
            print("You lose")

    elif dealer_score > player_score:
        if dealer_score <= 21:
            print("You lose")
        else:
            print("You win")
       
    elif player_score == dealer_score:
        print("It's a draw")

def dealCards():
    start_hand = random.sample(cards, 2) 
    return start_hand

while True:
    user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user_input == 'y':
        print(art.logo)
        player_deck = []
        dealer_deck = []
        
        # print(f"Initial player deck {player_deck}, initial dealer deck {dealer_deck}")

        
        player_deck.extend(dealCards())
        player_score = calculateScore(player_deck)
        print(f"Your cards: {player_deck}, Your current score:{player_score}")

        dealer_deck.extend(dealCards())
        dealer_score = calculateScore(dealer_deck)
        print(f"Computer's first card: {dealer_deck[0]}")
        
        if dealer_score == 21:
            print(f"Your final hand: {player_deck}, current score: {player_score}")
            print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
            print("You lose, opponent has blackjack!")
            break

        if player_score == 21:
            print(f"Your final hand: {player_deck}, current score: {player_score}")
            print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
            print("Blackjack! You win!")
            break


        while player_score < 21:
            play_again = input("Type 'y' to get another card, type 'n' to pass: ")
            if play_again == 'y':
                player_card = random.choice(cards)
                player_deck.append(player_card)
                player_score = calculateScore(player_deck)
                print(f"Your cards: {player_deck}, Your current score:{player_score}")
                print(f"Computer's first card: {dealer_deck[0]}")

            else:              
                break
    
        
        while dealer_score < 17:
            dealer_card = random.choice(cards)
            dealer_deck.append(dealer_card)
            dealer_score = calculateScore(dealer_deck)

        dealGame()

    else:
        break

# TODO, remove redundancy in displaying final cards
