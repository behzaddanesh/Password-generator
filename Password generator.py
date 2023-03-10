import random
import string

def generate_password(length):
    # Define the character set to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choices to generate a list of characters of the specified length
    password = ''.join(random.choices(characters, k=length))

    return password

# Prompt the user to enter a password length
password_length = int(input("Enter the desired length of the password: "))

# Call the generate_password function and print the result
new_password = generate_password(password_length)
print("Your new password is:", new_password)