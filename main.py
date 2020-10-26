from src.caesar import * 
from src.vigenere import *
from src.reverse import *

def main():
    print("Hello and welcome to my encryption game\n"
          "There are three difficulty levels, each using a different method of encryption.\n"
          "After that, you can take a test to prove that you are a master cryptographer!\n")

    while True:
        level = str(input("Enter 1, 2, or 3, to select a difficulty level, or enter Q to quit. "))
        if level == '1':
            reverse_main()
        elif level == '2':
            caesar_main()
        elif level == '3':
            vigenere_main()
        elif level.lower() == 'q':
            exit()
        else:
            pass


main()