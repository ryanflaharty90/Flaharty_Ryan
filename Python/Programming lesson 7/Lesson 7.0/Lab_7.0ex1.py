num = int(input("Please enter a number:"))
mun = num
Sum = 0

while num > 0:
    Sum += num%10
    num = int(num/10)

print("The total of the digits is", mun, "is", Sum)
    
    
    
