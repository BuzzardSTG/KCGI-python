"""
ID:M22W0064
Assingment #2 - student grade transformator
Name: VALERIJS KANEVS
Written on: 2023/5/7
"""

x = int(input("What is your score on the exam?\n"))
while True:
    if 0<= int(x) <=100:
        if x == 100 or x >= 90:
            print("A")
        elif x >= 80:
            print("B")
        elif x >= 70:
            print("C")
        elif x >= 60:
            print("D")
        else:
            print("F")
    else:
        print("Incorrect value inputted. Try again.")
    break;

# conditionals through range(start, stop)

z = int(input("What is your score on the exam?\n"))
if z in range(90,100):
    print("A")
elif z in range(80,89):
    print("B")
elif z in range(70,79):
    print("C")
elif z in range(60,69):
    print("D")
else:
    print("F")

# making a function that will test input for errors (try/except method)

def subject_grade(c):
    try:
        c = int(c)
        if c == 100 or c >= 90:
            print("A")
        elif c >= 80:
            print("B")
        elif c >= 70:
            print("C")
        elif c >= 60:
            print("D")
        else:
            print("F")
    except ValueError:
        return "Incorrect value. \nTry again in range 0-100"
c = input("What is your score on the exam?\n")
final_grade = subject_grade(c)
print(final_grade)


#For the array of values, I think we need to use the while loop on an array?
