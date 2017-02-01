def printf(calc):
    print("${:4.2f}".format(calc))


def calcPayment(pr,rn,ni,to):
    return ((pr*((1 + (rn/ni))**(ni*to)))/(12*to))

p = int(input("What is the principal cost"))
r = float(input("What is the interest rate"))
n = int(input("How moany times do you pay a year"))
t = int(input("What is the life of the loan"))

print(printf(calcPayment(p,r,n,t)))

