number = int(input("Please enter a number"))
size = int(input("Please enter the size of the table"))

print("___|___")
for i in range(1, size+2):
    print("{:>3}|{:<3}".format(i-1, number*i))
