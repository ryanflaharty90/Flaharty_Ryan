equation = input("Please enter an equation:")
equat = equation.split(" ")
print(equat)

i = 0
while i < len(equat):
    if i < len(equat) and (equat[i] == "*" or equat [i] == "/"):
        if equat[i] == "*":
            equat[i] = int(equat[i-1])* int(equat[i+1])
        else:
            equat[i] = int(equation[i-1])/ int(equat[i+1])
        print(equat)
        equat.pop(i-1)
        equat.pop(i)
    else:
        i += 1
i = 0
while i < len(equat):
    if i < len(equat) and (equat[i] == "+" or equat[i] == "-"):
        if equat[i] == "+":
            equat[i] = int(equat[i-1]) + int(equat[i+1])
        else:
            equat[i] = int(equat[i-1])-int(equat[i+1])
        equat.pop(i-1)
        equat.pop(i)
    else:
        i += 1
print(equat)
            
