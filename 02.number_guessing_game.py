# Import the random module to generate random numbers
import random

# Number Guessing Game
def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0  # Initialize the attempts counter

    # Continue the game until the correct number is guessed
    while True:
        try:
            # Get the user's guess as a floating-point number
            user_guess = float(input("Guess the number (1-100): "))
            
            # Validate that the guess is within the valid range
            if 1 <= user_guess <= 100:
                attempts += 1  # Increment the attempts counter

                # Check if the guess is correct
                if user_guess == number_to_guess:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    break
                # Provide hints if the guess is too low or too high
                elif user_guess < number_to_guess:
                    print("Too low. Try again.")
                else:
                    print("Too high. Try again.")
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the game by calling the number_guessing_game function
number_guessing_game()
