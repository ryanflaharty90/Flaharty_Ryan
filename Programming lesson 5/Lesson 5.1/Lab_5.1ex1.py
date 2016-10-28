g1 = input("What was your final grade?")
g2 = input("What was your final grade?")
g3 = input("What was your final grade?")
g4 = input("What was your final grade?")
g5 = input("What was your final grade?")
g6 = input("What was your final grade?")
g7 = input("What was your final grade?")

gradepoint = 0 

def grade(grade):
    global gradepoint
    if grade == "A":
        gradepoint = 4.0;
    if grade == "B":
        gradepoint = 3.0;
    if grade == "C":
        gradepoint = 2.0;
    if grade == "D":
        gradepoint = 1.0;
    if grade == "F":
        gradepoint = 0.0;
    return(gradepoint)

gpa = (grade(g1)+grade(g2)+ grade(g3)+ grade(g4)+ grade(g4)+ grade(g5)+ grade(g6)+ grade(g7))/7
print("Your GPA is", gpa)
