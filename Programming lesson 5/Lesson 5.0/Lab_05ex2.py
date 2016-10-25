def printf(item ,price):
    print("*{:<30}......{:>5.2f}".format(item, price))

item1 = input("Please enter the item")
price1 = float(input("Please enter the price"))
item2 = input("Please enter the item")
price2 = float(input("Please enter the price"))
item3 = input("Please enter the item")
price3 = float(input("Please enter the price"))
item4 = input("Please enter the item")
price4 = float(input("Please enter the price"))

print("<<<<<<<<<<reciept>>>>>>>>>>")

printf(item1, price1)
printf(item2, price2)
printf(item3, price3)
printf(item4, price4)

print("_" *30)
subtotal = price1 + price2 + price3 + price4
printf("Subtotal", subtotal)

tax = subtotal * .1
printf("Tax", tax)

discount = 0

def discount():
    global subtotal
    if subtotal >= 2000:
        discount = 100;
        return(discount)
    if subtotal <= 2000:
        discount = 0.0;
        return(discount)

total = subtotal + tax - discount();
printf("Total: ", total)































































