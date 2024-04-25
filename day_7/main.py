import random
from hangman_art import stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
from hangman_art import logo
print(logo)

display = ["_"] * word_length

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    print(stages[lives])


# output
# _                                             
# | |                                            
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |                      
#                    |___/    
# Guess a letter: a
# _ _ _ a _

#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========

# Guess a letter: r
# You guessed r, that's not in the word. You lose a life.
# _ _ _ a _

#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========

# Guess a letter: a
# You've already guessed a
# _ _ _ a _

#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========

# Guess a letter: g
# You guessed g, that's not in the word. You lose a life.
# _ _ _ a _

#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========

# Guess a letter: u
# You guessed u, that's not in the word. You lose a life.
# _ _ _ a _

#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========
# Guess a letter: i
# You guessed i, that's not in the word. You lose a life.
# _ _ _ a _

#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========

# Guess a letter: x
# You guessed x, that's not in the word. You lose a life.
# _ _ _ a _

#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========

# Guess a letter: b
# You guessed b, that's not in the word. You lose a life.
# You lose.
# _ _ _ a _

#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
