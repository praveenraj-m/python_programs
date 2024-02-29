import random  # Import the random module for generating random values
import string  # Import the string module for working with ASCII characters

# Function to generate a random password of a given length
def generate_random_password():
    # Get the desired password length from the user
    try:
      password = input("Enter the desired password length: ")
      password_length = int(password)
    except ValueError:
      print(f"Enter only numeric values to continue with password generation and not {password}")
      return generate_random_password()

    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Initialize an empty string to store the generated password
    password = ''

    # Loop to randomly choose characters and concatenate them to form the password
    for _ in range(password_length):
        random_character = random.choice(characters)  # Randomly choose a character
        password += random_character  # Concatenate the chosen character to the password

    # Return the generated password
    return password

# Call the function to generate and print the password
generated_password = generate_random_password()
print("Generated Password:", generated_password)
