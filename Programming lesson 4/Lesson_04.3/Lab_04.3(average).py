def calcAverage(num1, num2, num3):
    global avr;
    avr = float((num1+num2+num3)/3);

def printf():
    print("The average of the three numbers is {:5.5f}".format(avr))

Num1 = float(input("What is the first number?"))
Num2 = float(input("What is the second number?"))
Num3 = float(input("What is the third number?"))
  
calcAverage(Num1, Num2, Num3)
printf()
