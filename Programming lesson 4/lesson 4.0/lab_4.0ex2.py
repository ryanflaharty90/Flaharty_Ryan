def printf(item1, item2):
    print("*{:<20}{:>10}*".format(item1, item2))
    

fname = input("What is your first name?")
lname = input("What is your last name?")
title = input("What is your occupation at this school?")
school = input("What school will you be attending?")
year = input("What school year are you in?")
subject = input("What is your subject?")

print("*" *32)

printf(school, year)
printf(fname, lname)
printf(title, subject)

print("*" *32)
