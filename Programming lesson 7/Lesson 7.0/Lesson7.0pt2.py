sentence = input("please enter a string:")

top = 0
while top < sentence.count(" ") > 0:
    sentence = sentence[0 : sentence.index(" ")] + sentence[sentence.index(" ")+1 : len(sentence)]

print("Without spaces..." + sentence)
