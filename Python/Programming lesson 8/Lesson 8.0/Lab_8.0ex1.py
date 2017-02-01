sentence = input("Please enter a sentence:")

def replaceSpace(sen):
    if sen.count(" ") == 0:
        return sen
    else:
        return replaceSpace((sen[0:sen.index(" ")] + "_" + sen[sen.index(" ") + 1:len(sen)]))
    return sen

print(replaceSpace(sentence))

