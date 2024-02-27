import random

# Hangman Game
def hangman_game():
    words = ["python", "java", "programming", "computer", "hangman", "developer"]
    secret_word = random.choice(words)
    guessed_letters = set()
    max_attempts = 6
    attempts = 0

    while attempts < max_attempts:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_ "

        print("Current Word:", display_word)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in secret_word:
            print("Good guess!")
            guessed_letters.add(guess)
        else:
            print("Incorrect guess.")
            attempts += 1

        if set(secret_word) <= guessed_letters:
            print(f"Congratulations! You guessed the word: {secret_word}")
            break

    if attempts == max_attempts:
        print(f"Sorry, you ran out of attempts. The correct word was: {secret_word}")

# Run the Hangman Game
hangman_game()

