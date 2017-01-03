w = input("Please enter a word")
start = 1
stop = len(w)

def tree(w,start,stop):
    if start <= stop:
        print("{:>8}".format(w[0:start]))
        start = start + 1
        tree(w,start,stop)
    else:
        return " "

tree(w,start,stop)
        
        
