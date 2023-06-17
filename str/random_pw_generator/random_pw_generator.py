'''
Title:
Random Password Generator

Description:
Create a program that generates a random password of a specified length.

Details:
- The program should prompt the user to enter the desired length of the password.
- It should generate a random password consisting of a combination of letters (both uppercase and lowercase), digits, and punctuation marks.
- The generated password should have a length equal to the value entered by the user.
- Finally, the program should display the generated password to the user.'''

import string
import random

while True:
    user_input = input("Enter the desired password length:")

    try:
        pw_len = int(user_input)
    except:
        print("<!> Enter just a number")
        continue

    if pw_len > 0:
        break
    else:
        print("<!> Enter a number greater than 0")
        continue

pw = ''
char_set = string.ascii_letters + string.digits + string.punctuation

for _ in range(pw_len):
    pw += random.choice(char_set)

print("Generated password:", pw)