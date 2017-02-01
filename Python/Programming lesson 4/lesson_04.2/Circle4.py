def printf(area):
    print("Ther area of the circle is{:5.5f}".format(area))
    

R = float(input("What is the radius of the circle?"))

def area(r):
    return float(3.1415*(r**2))

printf(area(R))
