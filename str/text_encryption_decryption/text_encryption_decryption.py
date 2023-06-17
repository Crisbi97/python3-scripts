'''
Title:
Text Encryption and Decryption

Description:
Create a program that can encrypt and decrypt a given text using a simple cipher, such as a Caesar cipher.
The program should allow the user to enter a text and a shift value, and then perform encryption or decryption based on the user's choice.

Details:
1. Provide the user with options to choose between encryption and decryption.
2. Prompt the user to enter a text.
2. Ask the user to enter a shift value, which will determine the amount by which each character is shifted during encryption or decryption.

A. Implement the encryption process:
    Iterate through each character in the text.
    Check if the character is alphabetic.
    If alphabetic, determine the ASCII offset based on uppercase (A = 65) or lowercase (a = 97).
    Apply the shift value to the character, wrapping around the alphabet if necessary.
    Append the encrypted character to a new string.
    Maintain the non-alphabetic characters as they are.
Display the encrypted text to the user.

B. Implement the decryption process:
    Iterate through each character in the encrypted text.
    Check if the character is alphabetic.
    If alphabetic, determine the ASCII offset based on uppercase or lowercase.
    Reverse the shift value to decrypt the character, wrapping around the alphabet if necessary.
    Append the decrypted character to a new string.
    Maintain the non-alphabetic characters as they are.
    Display the decrypted text to the user.
'''

def caesar_cipher(text, shift, flag):
    crypted_text = ''
    text = text.strip()

    #0 = encrypt; 1 = decrypt
    if flag: shift = -shift

    for char in text:
        if char.isalpha():
            if char.isupper(): ascii_offset = 65
            else: ascii_offset = 97

            #char_index = (a || A = 0, b || B = 1, ...)
            char_index = ord(char) - ascii_offset
            #encrypt_index = (char=D, shift = 1000) = ((3 + 1000) % 26) + 65 = 1003%26 + 65 = 15 + 65 = 80 > 'P'
            crypted_index = ((char_index + shift) % 26) + ascii_offset

            crypted_text += chr(crypted_index)
        else:
            crypted_text += char

    return crypted_text



text = input("Enter the text: ")

while True:
    shift = input("Enter the shift value: ")

    try:
        shift = int(shift)
        break
    except:
        print("<!> Enter a number.")
        continue

while True:
    flag = input("Enter '0' to encrypt or '1' to decrypt: ")

    try:
        flag = int(flag)
    except:
        print("<!> Enter a number.")
        continue

    if flag == 0 or flag == 1:
        break
    else:
        print("<!> Number not valid")
        continue

crypted_text = caesar_cipher(text, shift, flag)
print("Result:", crypted_text)

