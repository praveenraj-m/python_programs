# Program that Accepts a Sentence and Calculates the Number of Letters and Digits
def count_letters_digits(sentence):
    letters = 0
    digits = 0

    for char in sentence:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1

    return letters, digits

# Example usage
user_input = input("Enter a sentence: ")
letter_count, digit_count = count_letters_digits(user_input)

print(f"Number of letters: {letter_count}")
print(f"Number of digits: {digit_count}")
