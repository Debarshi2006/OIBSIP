import random
import string

def main():
    print("--- Simple Python Password Generator ---")

    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    
    letters = string.ascii_letters  
    numbers = string.digits         
    symbols = string.punctuation    

    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    char_pool = letters
    if include_numbers:
        char_pool += numbers
    if include_symbols:
        char_pool += symbols


    password = ""
    for _ in range(length):
        random_char = random.choice(char_pool)
        password += random_char

    print(f"\nYour generated password is: {password}")

if __name__ == "__main__":
    main()