""" Grade from Marks  EASY Hint: 90+ A, 75+ B, 60+ C, 40+ D, else F. 
Check from highest to lowest so each else-if
 only runs when the one above failed."""

def check_marks(marks):
    if marks>=90:
        return("A")
    elif marks>=75:
        return("B")
    elif marks>=60:
        return("C")
    elif marks>=40:
        return("D")
    else:
        return("F")

marks= float(input("Enter the Marks "))
print(check_marks(marks))


#better 
def check_marks(marks):
    if not 0 <= marks <= 100:
        return "Invalid marks"

    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    return "F"


try:
    marks = float(input("Enter marks (0-100): "))
    print(check_marks(marks))
except ValueError:
    print("Please enter a valid number.")