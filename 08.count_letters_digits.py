# Program that Accepts a Sentence and Calculates the Number of Letters and Digits
def count_letters_digits(sentence):
    # Initialize counters for letters and digits
    letters = 0
    digits = 0

    # Iterate through each character in the sentence
    for char in sentence:
        # Check if the character is a letter
        if char.isalpha():
            letters += 1
        # Check if the character is a digit
        elif char.isdigit():
            digits += 1

    # Return the counts
    return letters, digits

# Example usage
user_input = input("Enter a sentence: ")
letter_count, digit_count = count_letters_digits(user_input)

# Print the results
print(f"Number of letters: {letter_count}")
print(f"Number of digits: {digit_count}")
