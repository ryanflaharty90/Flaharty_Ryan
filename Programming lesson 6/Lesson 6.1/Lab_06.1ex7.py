w = input("Please enter a word:")

def printTri():
    for i in range(len(w), -1, -1):
        print(w[i:len(w)])
printTri()
        
