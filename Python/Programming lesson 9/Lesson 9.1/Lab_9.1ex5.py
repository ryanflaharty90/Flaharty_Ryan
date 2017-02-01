numbers = [2,6,8,9,10,12,13,15,17,24,55,66,78,77,79]

def gFactor(number):
    for i in range(2, number):
        if number % i == 0:
            return 1
    return 0
def removePrimes(num):
    for n in num:
        if gFactor(n) == 0:
            num.remove (n)

removePrimes(numbers)
print(numbers)
