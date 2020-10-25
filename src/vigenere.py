import random
import itertools
from helper import *

def vigenere_encryption(mode, text, key=None):
    """
    This function takes a text and encrypts or decrypts it according to the key word provided. 
    It takes 3 parameters:
        1) "mode" tells the function to encrypt (add the key value) or decrypt (subtract the key value)
        2) "text": the string to be encrypted or decrypted
        3) "key": the string that will be used to decrypt the message.  When encrypting, the key is random.
    """
    mode = mode
    text = text.lower()
    keys = []
    new_lst = []
    if mode == 'encrypt':
        key = random.choice(cipher_key)
        print("Your key is :", key)
    elif mode == 'decrypt':
        key = key
    k = itertools.cycle(key)  
    # creates an infinite iteration over the key creating a list as long as the text from the variable k
    # Como no sabemos la longitud del string que nos van a pasar utilizamos itertools.cycle como un "puntero infinito"
    i = 1
    while i <= len(text):
        keys.append(next(k))
        i += 1
    #print("Key list: ", keys)
    num_list = [abc_to_num[s] if s in abc else s for s in text]
    num_key_list = [abc_to_num[s] for s in keys]
    for num1, num2 in zip(num_list, num_key_list):
        if num1 in num:
            #num in helper.py range (0,54)
            if mode == 'encrypt':
# adds the numeric values of the text and key together
                #print("Sum: ", num1, " + ", num2)
                new_lst.append(num1 + num2)
            elif mode == 'decrypt':
# subtracts the numeric values of the text and key together
                #print("Substract: ", num1, " - ", num2)
                new_lst.append(num1 - num2)
        else:
            new_lst.append(num1)
    decoded_list = [num_to_abc[n % 54] if isinstance(n, int) else n for n in new_lst]
    new_str = ""
    for i in decoded_list:
        new_str += i
    return new_str

def vigenere_main():
    """Asks user if they want to practice (encode or decode) or take the test, and calls the corresponding function."""
    while True:
        print('Type Q to quit or M to return to the main menu.')
        pt = input('would you like to practice or take the test? P/T ')
        if pt.lower() == 'p':
            choice = input('Would you like to encrypt or decrypt? E/D ')
            if choice.lower() == 'e':
                text = input('Enter the text you would like to encode: ')
                message = vigenere_encryption('encrypt', text)
                print('Your encrypted text is :' + message)
            elif choice.lower() == 'd':
                text = input('Enter the text you would like to decode: ')
                key = input('Enter the key: ')
                message = vigenere_encryption('decrypt', text, key)
                print('Your decrypted text is :' + message)
            else:
                print('You must enter either "E" or "D" to encode or decode a text. ')
        elif pt.lower() == 't':
            text = random.choice(text_list)
            encrypted_text = vigenere_encryption('encrypt', text)
            print(encrypted_text)
            answer = input('Can you decode this string? ')
            if answer.lower() == text.lower():
                print('Yay! You solved level 3!\n')
                break
            elif answer.lower() != text.lower():
                print("Sorry, you failed. Don't worry, you just need a little more of practice.\n")
            elif pt.lower() == 'q':
                exit()
            elif pt.lower() == 'm':
                break
        else:
            print('Please enter a valid choice.')