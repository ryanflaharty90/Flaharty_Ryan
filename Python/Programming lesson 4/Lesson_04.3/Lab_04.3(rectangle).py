def printf():
    print("Your rectangle is {:5.5f} feet around".format(perimeter))

L = float(input("What is the length of the rectangle?"))
W = float(input("What is the width of the rectangle?"))

def calcPerim(l,w):
    global perimeter;
    perimeter = ((l*2)+(w*2))

calcPerim(L,W)
printf()


