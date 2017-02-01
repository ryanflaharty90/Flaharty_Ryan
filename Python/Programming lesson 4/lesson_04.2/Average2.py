def printf(num):
    print("{:2.2f}".format(num))



num1 = int(input("Enter number 1"))
num2 = int(input("Enter number 2"))
num3 = int(input("Enter number 3"))

def average():
    print(num1 + num2 + num3/3)

print("The average is", (num1 + num2 + num3)/3)
