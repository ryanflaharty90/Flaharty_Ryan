w1 = input("please enter a word:")
w2 = input("please enter a word:")
w3 = input("please enter a word:")

def makeCenter(w):
    if len(w) >= 20:
        return w
    else:
        return makeCenter(" "+ w +" ")
    
print(makeCenter(w1))
print(makeCenter(w2))
print(makeCenter(w3))
