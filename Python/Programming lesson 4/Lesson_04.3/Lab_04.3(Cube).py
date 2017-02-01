sa = 0
L = float(input("What is the length of the cube"))
W = float(input("What is the width of the cube"))
H = float(input("What is the height of the cube"))

def calcSurfarea(l, w, h):
    global sa
    sa= l*w*h

def printf():
    print("The surface area of the cube is {:5.5f}".format(sa))


calcSurfarea(L, W, H)
printf()
