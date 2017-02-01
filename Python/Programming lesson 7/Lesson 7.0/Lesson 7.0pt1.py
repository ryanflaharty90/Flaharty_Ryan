number = int(input("Please enter a number:"))
digits = 0



while number > 0:
    digits += 1
    number = int(number / 10)

print("There are ", digits, "digits in ", number)
