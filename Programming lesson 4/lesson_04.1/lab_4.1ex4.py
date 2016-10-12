def printf(volume):
    print("{:4.2f}".format(volume))

def volBox(h,l,w):
    return float(h*w*l)


hi = int(input("What is the height?"))
le = int(input("What is the length?"))
wi = int(input("What is the width?"))

printf(volBox(hi,wi,le))

