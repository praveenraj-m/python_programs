import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
password_length = 12
generated_password = generate_random_password(password_length)
print("Generated Password:", generated_password)
