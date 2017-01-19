start = int(input("Please enter a starting number"))
size = int(input("Please enter the size of your sequence"))
sequence = []
for i in range(0,size):
    if i==0 or i==1:
        sequence.append(start)
    else:
        seq.append(sequence[i-1] + sequence[i-2])
print(sequence)
