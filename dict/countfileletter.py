'''
Write a Python program that takes a text file as input and returns the number of words of a given text file.
Print in reverse order
Note: filer the non word char: ",;.:?!"
'''

charDict = dict()
orderList = list()



#openint the file
while True:
    print("Press enter to quit")
    fname = input("Enter file name:")

    if len(fname) < 1:
        quit()

    if ".txt" not in fname:
        print("File must be .txt")
        continue

    try:
        file = open(fname)
        break
    except:
        print("File not found")
        continue

#for every line (string) in the file
for line in file:

    #remove the line left ,right spaces
    line = line.strip()

    #for every word (string) in the line (string)
    for word in line.split():

        #remove ",;.:?!" from right side of the word and upper
        word = word.rstrip(",;.:?!")
        word = word.upper()

        #for every char (string single digit = "char")
        for char in word:

            #if the char is alpha (no number, no simbols)
            if char.isalpha():
                #add and count the occurrence in the dict (char is key, count is value)
                charDict[char] = charDict.get(char, 0) + 1

#append in a list the tuple (char, count) but inverted (count, char) so it is possible to order by count
for char, count in charDict.items():
    orderList.append((count,char))

#order the list by count in reverse (bigger to smaller)
orderList.sort(reverse=True)

#print the list occurrences: char, count
for count, char in orderList:
    print("The letter", char, "occurs", count, "times")


