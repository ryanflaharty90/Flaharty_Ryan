def printf(money):
    output = "*{:>4.0}$".format(money)
    return output

r = .23
P = 1000
n = 12
t = 5
A = P*(1 + r/n)**n*t

print(format(A))

