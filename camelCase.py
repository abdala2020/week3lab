def display_banner():
    """ Display program name in banner """
    msg = 'AWSOME  camelCaseGenerator PROGRAM'
    stars = '*' + len(msg) 
    print(f'\n {stars} \n {msg} \n {stars}\n' )
display_banner()


sentence = "fOnt proCESSOR and ParsER"
splitSentence = sentence.split()
myList = [splitSentence[0].lower()]
word = ""
print(splitSentence)
for i in range(1, len(splitSentence)):
    word = splitSentence[i].capitalize()
    myList.append(word)
print("".join(myList))