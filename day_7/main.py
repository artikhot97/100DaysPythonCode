import random
from hangman_words import word_list
from hangman_art import stages

chosen_word = random.choice(word_list)

display = ["_"] * len(chosen_word)
lives = 6
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
  
    if guess not in chosen_word:
       print(f"You guessed {guess}, that's not in the word. You lose a life.")
         lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")
  
    if "_" not in display:
        end = True
        print("You Win")
        
    print(stages[lives])
