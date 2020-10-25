![](https://platform6.io/wp-content/uploads/2019/03/Bloc-post_Protecting-data-through-encryption.jpg)

# **Game-Project**
### What's this project about?
In this project I've created a game to encrypt or decrypt the text you provide the program with.
### How does it work?
We have three different levels in this game:
1.  #### Reverse encryption:
This mode reverses the order of a string, so the parameter should be a string.\
**For example**, if you are encrypting the text 'Such an awesome project', the encrypted text would be 'tcejorp emosewa na hcuS!

2. #### Caesar encryption:
This mode like the Caesar Cipher takes a string, and converts each letter in the string to a different one by associating it with a number, and uses the key to get a new numeric value that is then translated back into a new encrypted string.\
   **For example**, if you are encrypting the text 'abc', and your key is 1, the encrypted string would be 'bcd' because
    a = 0, b = 1, c = 2, d = 3 ... and the key of 1 adds 1 to the number corresponding number of each letter in the
    text.\
    The function takes 3 parameters:
    1) "mode" tells the function to encrypt (add the key value) or decrypt (subtract the key value)\
    2) "text" is the text to be encrypted or decrypted\
    3) "key" is the numeric key that will be used to decrypt your message.  If you are encrypting, the key is
            random.

[Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)

3. #### Vigenère encryption:
This mode takes a text and encrypts or decrypts it according to the key word provided. The
    function used to encrypt/decrypt
    uses a key-word changed into a series of numbers that is then applied to the text.\
    

**For example**, if you are encrypting the text 'abc', and your key is 'bad', the encrypted string would be 'bbf'
    because a = 0, b = 1, c = 2, d = 3 ... and the key of 'bad' adds the series of numbers (1, 0, 3) to  to the text
    translated into numbers (0, 1, 2), which adds up to (1, 1, 5) or 'bbf'.\
    The function takes 3 parameters:
    1) "mode" tells the function to encrypt (add the key value) or decrypt (subtract the key value)
    2) "text" is the string to be encrypted or decrypted
    3) "key" is the string that will be used to decrypt your message.  If you are encrypting, the key is random.
    
The dictionaries that convert between letters and numbers are stored in the helper.py file.

[Vigenère Cipher](https://en.wikipedia.org/wiki/Vigenère_cipher)

### What can I do?
You can practise your encryption skills with the three methods trying to guess how will it work, and then, when you have practiced enough, you can try to test yourself with the test mode, so you will receive an encrypted text and you will have the chance to decrypt it.
