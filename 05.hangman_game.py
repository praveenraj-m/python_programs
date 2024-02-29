import random

# Hangman Game
def hangman_game():
    # List of words to choose from
    words = ["python", "java", "programming", "computer", "hangman", "developer"]

    # Randomly select a word from the list
    secret_word = random.choice(words)

    # Set to store guessed letters
    guessed_letters = set()

    # Maximum attempts allowed
    max_attempts = 6
    attempts = 0  # Counter for the number of attempts

    # Main game loop
    while attempts < max_attempts:
        display_word = ""

        # Build the word to display, replacing unguessed letters with underscores
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_ "

        # Print the current state of the word
        print("Current Word:", display_word)

        # Get a letter guess from the user
        guess = input("Guess a letter: ").lower()

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        # Check if the guessed letter is in the secret word
        elif guess in secret_word:
            print("Good guess!")
            guessed_letters.add(guess)
        else:
            print("Incorrect guess.")
            attempts += 1

        # Check if all letters in the secret word have been guessed
        if set(secret_word) <= guessed_letters:
            print(f"Congratulations! You guessed the word: {secret_word}")
            break

    # If the maximum attempts are reached
    if attempts == max_attempts:
        print(f"Sorry, you ran out of attempts. The correct word was: {secret_word}")

# Run the Hangman Game
hangman_game()
