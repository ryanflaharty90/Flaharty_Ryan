w = ["Mikey", "Joe", "Paul", "Leo", "Ricky"]
print("In order...")
output = ""
for i in w:
    output += i + " "
print(output)

print(" ")
print("Reversed")


def reverse(word):
    a = ""
    for i in range(len(w)-1,-1,-1):
        a += word[i]+ " "
    print(a)

reverse(w)


