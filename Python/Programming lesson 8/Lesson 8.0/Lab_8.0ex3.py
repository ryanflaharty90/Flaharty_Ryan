num = int(input("Please enter a number"))

def lucky(number):
    if number > 0:
        if number%10 == 7:
            return 1+ lucky(int(number/10))
        else:
            return 0+ lucky(int(number/10))
    else:
        return 0

print(lucky(num))
