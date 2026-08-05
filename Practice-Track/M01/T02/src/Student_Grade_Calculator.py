marks = int(input())

# Check whether the marks are valid and display the grade
if marks <= 100 and marks >= 90:
    print("Grade: A")
elif marks <= 89 and marks >= 75:
    print("Grade: B")
elif marks <= 74 and marks >= 60:
    print("Grade: C")
elif marks <= 59 and marks >= 40:
    print("Grade: D")
elif marks <= 39 and marks >= 0:
    print("Grade: F")
else:
    print("Fail")