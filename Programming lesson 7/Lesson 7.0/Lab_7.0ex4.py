sentence = input("Please enter a sentence:")

def replaceAt():
    global sentence
    while sentence.count("at") > 0:
        sentence = sentence.replace("at","@")
replaceAt()
print(sentence)
