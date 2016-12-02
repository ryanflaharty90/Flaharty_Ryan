
def averagedigits(number):
    global average
    digits = 0
    base = 0
    num = numbr
    while num > 0:
        digits += 1
        base += num%10
        num = int(num/10)
    average = base/digits

numbr = int(input("Enter a number"))
average = 0

averagedigits(numbr)

print("The average of the digits in", numbr," is ", average)
