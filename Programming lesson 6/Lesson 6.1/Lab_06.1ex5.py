number1 = int(input("Please enter a number"))
number2 = int(input("Please enter a number"))
final = " "

for i in range(number2, number1+number2, number2):
    final = final + str(i) + "\t"
print(final)
