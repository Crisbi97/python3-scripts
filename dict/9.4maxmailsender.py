'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of timesthey appear in the file.
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''
senderCount = dict()

#open file
while True:
    fname = input("Enter file name:")

    try:
        file = open(fname)
        break
    except:
        print("404")
        continue

#scanning file lines
for line in file:
    line = line.strip()

    #checking lines with "From" and not "From:"
    if "From" in line:

        if "From:" in line:
            continue

        #splitting the line in words
        words = line.split()
        #checkig if the second word is a valid sender address
        if "@" in words[1]:
            senderCount[words[1]] = senderCount.get(words[1], 0) + 1

#couting the max sender
maxSender = None
maxMail = None
for sender, mail in senderCount.items():

    if maxMail is None:
        maxSender = sender
        maxMail = mail

    elif mail > maxMail:
        maxSender = sender
        maxMail = mail

print(maxSender, maxMail)


