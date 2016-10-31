h = float(input("What is your height(in)?"))
w = float(input("What is your weight(lbs)?"))

def bmi(h,w):
    return(703*(w/(h**2)))

print(bmi(h,w))

if bmi(h,w) < 18.5:
    condition = "You are underweight"

elif bmi(h,w) < 25:
    condition = "You have normal BMI"

elif bmi(h,w) < 29.9:
    condition = "You are a bit overweight"
    
elif bmi(h,w) < 34.9:
    condition = "Maybe some cardio?"

elif bmi(h,w) < 39.9:
    condition = "Cut the junk food"

else:
    condition = "You need help"


print(condition)
