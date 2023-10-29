


import random
import string

def password_generator(password_length, use_lowercase, use_uppercase, use_digits, use_symbols):
    # Define the character sets for the password based on the input
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()_+=-"

    # Use random.choices() to generate a password of the desired length
    password = "".join(random.choices(characters, k=password_length))
    return password

# Prompt the user for the desired password length
password_length = int(input("Enter desired password length: "))

# Prompt the user for the character sets to include in the password
use_lowercase = input("Include lowercase characters? (y/n): ").lower() == "y"
use_uppercase = input("Include uppercase characters? (y/n): ").lower() == "y"
use_digits = input("Include digits? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"
print()
print()

print("Your password = "+ password_generator(password_length,use_lowercase,use_uppercase,use_digits,use_symbols))
