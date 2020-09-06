sentence = "fOnt proCESSOR and ParsER"
splitSentence = sentence.split()
myList = [splitSentence[0].lower()]
word = ""
print(splitSentence)
for i in range(1, len(splitSentence)):
    word = splitSentence[i].capitalize()
    myList.append(word)
print("".join(myList))