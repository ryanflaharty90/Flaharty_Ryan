import random
numbs = []
for i in range (0,10):
    numbs.append(random.randint(1,100))
print("Numbers:")

output = ""
for v in numbs:
    output += str(v) +" "
print(output)

print("")

def average(nums):
    ave = 0
    for x in nums:
        ave += x
    return (ave/10)

print(" The average of the number above is:", average(numbs))


