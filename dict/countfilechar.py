'''
Input:.txt file
Output: print in reverse order (descending) in command line the number of occurrence of char (letters (cap) and numbers)
> 'The char X occurs Y times'

Note: filer the non word char: ",;.:?!"
'''

# dict for letters
alphaDict = dict()
# dict for num
numDict = dict()


#openint the file
while True:
    print("[press enter to quit]")
    fname = input("Enter file name:")

    # quit cmd
    if len(fname) < 1:
        quit()

    # check .txt extension
    if ".txt" not in fname:
        print("File must be .txt\n")
        continue

    # check open file
    try:
        file = open(fname)
        break
    except:
        print("File not found\n")
        continue

# for every line (string) in file.txt
for line in file:

    # remove left ,right spaces in line
    line = line.strip()

    # for every word (string) in the line (string)
    for word in line.split():

        # remove ",;.:?!" from right side of the word and upper
        word = word.rstrip(",;.:?!")
        word = word.upper()

        # for every char (string single digit = "char")
        for char in word:

            # if the char is alpha (no number, no simbols)
            if char.isalpha():
                # add and count the occurrence in the dict (char is key, count is value)
                alphaDict[char] = alphaDict.get(char, 0) + 1

            elif char.isnumeric():
                # add and count the occurrence in the dict (char is key, count is value)
                numDict[char] = numDict.get(char, 0) + 1

# check if any letters
if len(alphaDict) > 0:

    # list to order dict tuple based on key = count
    orderList = list()

    # 1. sorting alpha
    # append in a list the tuple (char, count) but inverted (count, char) so it is possible to order by count
    for char, count in alphaDict.items():
        orderList.append((count, char))

    # order the list by count in reverse (bigger to smaller)
    orderList.sort(reverse=True)

    print("Occurrences of letters in", fname + ":")
    # print the list occurrences: char, count
    for count, char in orderList:
        print("The letter", char, "occurs", count, "times")
else:
    print("No letters found in", fname + ":")

# check if any num
if len(numDict) > 0:

    orderList = list()

    # 2. sorting num
    # append in a list the tuple (char, count) but inverted (count, char) so it is possible to order by count
    for char, count in numDict.items():
        orderList.append((count, char))

    # order the list by count in reverse (bigger to smaller)
    orderList.sort(reverse=True)

    print("Occurrences of numbers in", fname + ":")
    # print the list occurrences: char, count
    for count, char in orderList:
        print("The number", char, "occurs", count, "times")

else:
    print("No numbers found in", fname + ":")

print("Good bye :)")
quit()