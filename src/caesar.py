import random
from helper import *
   
def cae_encrypt(mode, text, key=None):
    """
    This function, like the Caesar Cipher takes a string, and converts each letter to a different one 
    by associating it with a number. Then, uses the key to get a new numeric value that is then translated back 
    into a new encrypted string.
    It takes 3 parameters:
        1) "mode" tells the function to encrypt (add the key value).
        2) "text": the text to be encrypted or decrypted.
        3) "key": the numeric key that will be used to decrypt the message.The key is random when encrypting.
    """
    num_list = [abc_to_num[s] if s in abc else s for s in text]
    if mode == 'encrypt':
        key = random.randint(1, 53)
        print("Your key is :", key)
        new_lst = [num_to_abc[(n + key) % 54] if n in num else n for n in num_list]
        new_str = ''
    for i in new_lst:
        new_str += i
    return (new_str,)

def cae_decrypt(mode, text, key=None):
    """
    This function decrypts a text encrypted with the Caesar Cipher subtracting the key value.
    It takes 3 parameters:
        1) "mode" tells the function to encrypt (add the key value).
        2) "text": the text to be encrypted or decrypted.
        3) "key": the numeric key that will be used to decrypt the message.The key is random when encrypting.
    """
    mode = mode
    num_list = [abc_to_num[s] if s in abc else s for s in text]
    if mode == 'decrypt':
        key = key
        print("Your key for decryption is :", key)
        str_key = str(key)
        text = text.lower()
        new_lst = [num_to_abc[(n - key) % 54] if n in num else n for n in num_list]
        new_str = ''
    for i in new_lst:
        new_str += i
    return (new_str,)

def caesar_main():
    """Asks user if they want to practice (encode or decode) or take the test, and calls the corresponding function."""
    while True:
        print('Type Q to quit or M to return to the main menu.')
        pt = input('would you like to practice or take the test? P/T ')
        if pt.lower() == 'p':
            choice = input('Would you like to encrypt or decrypt? E/D ')
            if choice.lower() == 'e':
                text = input('Enter the text you would like to encode: ')
                message = cae_encrypt('encrypt', text)
                print('Your encrypted text is :' + message[0])
            elif choice.lower() == 'd':
                text = input('Enter the text you would like to decode: ')
                key = int(input('Enter the key: '))
                message = cae_decrypt('decrypt', text, key)
                print('Your decrypted text is :' + message[0])
            else:
                print('You must enter either "E" or "D" to encode or decode a text. ')
        elif pt.lower() == 't':
            text = random.choice(text_list)
            encrypted_text = cae_encrypt('encrypt', text)
            print(encrypted_text[0])
            answer = input('Can you decode this string? ')
            if answer.lower() == text.lower():
                print('Yay! You solved level 2!\n')
                break
            elif answer.lower() != text.lower():
                print("Sorry, you failed. Don't worry, you just need a little more of practice.\n")
        elif pt.lower() == 'q':
            exit()
        elif pt.lower() == 'm':
            break
        else:
            print('Please enter a valid choice.')