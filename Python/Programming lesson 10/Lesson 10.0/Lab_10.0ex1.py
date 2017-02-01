import random
numberList = []

for i in range (0,4):
    numberList.append([])
    for j in range(0,4):
        numberList[i].append(random.randint(1,100))

for nums in numberList:
    output = ""
    for num in nums:
        output += str(num) + " "
    print(output)
