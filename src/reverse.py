import random
from helper import *

def reverse(text):
    """
    This function reverses the order of a string, so the parameter "text" should be a string.
    """
    text = text
    reverse_str = text[::-1]
    return reverse_str

def reverse_main():
    """Asks user if they want to practice (encode or decode) or take the test, and calls the corresponding function."""
    while True:
        print('Type Q to quit or M to return to the main menu.')
        pt = input('would you like to practice or take the test? P/T ')
        if pt.lower() == 'p':
            choice = input('Would you like to encrypt or decrypt? E/D ')
            if choice.lower() == 'e':
                text = input('Enter the text you would like to encode: ')
                message = reverse(text)
                print('Your encrypted text is :' + message)
            elif choice.lower() == 'd':
                text = input('Enter the text you would like to decode: ')
                message = reverse(text)
                print('Your decrypted text is :' + message)
            else:
                print('You must enter either "E" or "D" to encode or decode a text. ')
        elif pt.lower() == 't':
            text = random.choice(text_list)
            encrypted_text = reverse(text)
            print(encrypted_text)
            answer = input('Can you decode this string?')
            if answer == text:
                print('Yay! You solved level 1!\n')
                break
            else: 
                print("Sorry, you failed. Don't worry, you just need a little more of practice.\n")
        elif pt.lower() == 'q':
            exit()
        elif pt.lower() == 'm':
            break
        else:
            print('Please enter a valid choice.')