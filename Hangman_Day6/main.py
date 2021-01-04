import random, hangman_art, hangman_words

game_words = ['avenue', 'awkward', 'delete', ] 
chosen_word = random.choice(game_words)
chosen_word_length = len(chosen_word)
blanks = []
player_lives = 6 

print(hangman_art.logo)

# print(f'The chosen word is {chosen_word}')

# Creating blanks according to length of the letter "_"
for _ in range(chosen_word_length):
    blanks.append("_")

# print(blanks)

# The game stops only when the two conditions are not met.
while "_" in blanks and player_lives > 0:
    # The player to guess a letter
    player_guess = input("Guess any letter you wish(wisely): ").lower()
 
    # Check if the player already guessed that letter
    if player_guess in blanks:
        print(f'You have already guessed letter {player_guess}, move on!👾')

    for i in range(chosen_word_length):
        if player_guess == chosen_word[i]:
            blanks[i] = player_guess

    if player_guess not in chosen_word:
        player_lives -= 1
        print(f"Letter {player_guess} is not in the word. You lose a life😰.")

    current_game = ''
    print(' '.join(blanks))
    print(hangman_art.stages[player_lives])

if "_" not in blanks:
    print('You win!🍰🥳')
else:
    print('You lose! Your man is left to hang☠️.')
    print(f"The word was {chosen_word}.")
