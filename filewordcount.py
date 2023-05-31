dCount = dict()

#open file
while True:
    fname = input("Enter file name:")
    try:
        file = open(fname)
        break
    except:
        print("404")
        continue

#counting words
for line in file:
    line = line.strip()
    #line = line.strip(".")
    #line = line.strip(",")

    for word in line.split():
        word = word.replace(".", "")
        word = word.replace(",", "")
        dCount[word] = dCount.get(word, 0) + 1

#print
for key, value in dCount.items():
    print("["+key+"]", "has occurred", value, "times")
