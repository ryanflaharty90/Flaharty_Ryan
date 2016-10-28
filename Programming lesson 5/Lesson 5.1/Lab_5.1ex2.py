h = float(input("What is your height(in)?"))
w = float(input("What is your weight(lbs)?"))

def bmi(h,w):
    return(703*(w/(h**2)))

print(bmi(h,w))

if bmi < 18.5:
    print("You are underweight")

if 18.5 < bmi < 24.9:
    print("You have normal BMI")

if 25 <= bmi <= 29.9:
    print("You are a bit overweight")

if 30 <= bmi <= 34.9:
    print("Dude hit the gym")

if 35 <= bmi <= 39.9:
    print("Cut the junk food")

if 40 <= bmi:
    print(":(")
