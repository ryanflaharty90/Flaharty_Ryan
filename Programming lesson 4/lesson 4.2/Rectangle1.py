def printf(perim):
       print("Your rectangle is {:5.2f} feet around".format(perim))

L = float(input("Please enter the length of the rectangle"))
W = float(input("Please enter the width of the rectangle"))

def calcPerim(l,w):
        return float((l*2)+(w*2))

printf(calcPerim(L,W))
