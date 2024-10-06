import random

def select_words():
    words = ["python", "hangman", "programming", "code","developer", "computer", "science","codealpha","world"]
    return random.choice(words)

def display_current_state(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    while True:
        word = select_words()
        guessed_letters = set()
        incorrect_guesses = 0
        max_incorrect_guesses = 10

        print("Welcome to Hangman!")
        
        while incorrect_guesses < max_incorrect_guesses:
            current_state = display_current_state(word, guessed_letters)
            print(f"Current word: {current_state}")
            print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")
            
            guess = input("Guess a letter: ").lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue
            
            if guess in guessed_letters:
                print("You've already guessed that letter.")
                continue
            
            guessed_letters.add(guess)
            
            if guess not in word:
                incorrect_guesses += 1
                print(f"Sorry, '{guess}' is not in the word.")
            else:
                print(f"Good job! '{guess}' is in the word.")
            
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You've guessed the word: {word}")
                break
        else:
            print(f"Game over! The word was: {word}")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    hangman()
