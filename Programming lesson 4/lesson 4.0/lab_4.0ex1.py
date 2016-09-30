
def printf(item, price):
    print("*{:<30}......{:>5.2f}".format(item, price))

item1 = input("Please enter item")
price1 = float(input("Please enter the price"))
item2 = input("Please enter item")
price2 = float(input("please enter the price"))
item3 = input("please enter item")
price3 = float(input("Please enter the price"))

print("<<<<<<<<Receipt>>>>>>>>")

printf(item1, price1)
printf(item2, price2)
printf(item3, price3)

print("_" *20)
subtotal = price1 + price2 + price3
printf("Subtotal", subtotal)
tax = subtotal * .1
printf("Tax", tax)
total = subtotal + tax
printf("Total", total)












