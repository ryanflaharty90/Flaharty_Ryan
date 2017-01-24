import random
xOo = []

for i in range (0,4):
    xOo.append([])
    for j in range (0,4):
            switch = random.randint(0,1)
            if switch == 1:
                xOo[i] += "X"
            else:
                xOo += "O"
for i in xOo:
    output = ""
    for j in i:
        output += j
    print(output)
