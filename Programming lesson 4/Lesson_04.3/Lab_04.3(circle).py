area = 0
R= float(input("What is the radius of the circle?"))

def calcArea(r):
    global area;
    area = float(3.1415*(r**2));

def printf():
    print("The area of the circle is {:5.5f}".format(area))

calcArea(R)
printf()
