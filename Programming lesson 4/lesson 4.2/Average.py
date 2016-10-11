def printf(num):
    print("The average is{:5.2f}".format(num))


num1 = float(input("Enter number 1"))
num2 = float(input("Enter number 2"))
num3 = float(input("Enter number 3"))

def average(n1,n2,n3):
    return float((n1 + n2 + n3)/3)
            
printf(average(num1,num2,num3))
