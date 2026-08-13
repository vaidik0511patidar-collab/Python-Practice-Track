student_name = input()
marks = []

# Read mark from user and store it in marks[]
for mark in range(5):
    mark = int(input())
    marks.append(mark)

# Calculate total marks, average, highest, lowest, number of subjects passed and number of subjects failed
total_marks = 0
highest = marks[0]
lowest = marks[0]

for mark in marks:
    total_marks += mark

    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

average = total_marks / 5

pass_count = 0
fail_count = 0

for mark in marks:
    if mark >= 40:
        pass_count += 1
    else:
        fail_count += 1

# Determine the final grade using average
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 40:
    grade = 'D'
else:
    grade = 'F'

# Display Results
print(f"Student Name: {student_name}")
print(f"Marks: {marks}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")
print(f"Subjects Passed: {pass_count}")
print(f"Subjects Failed: {fail_count}")
print(f"Final Grade: {grade}")

# Display marks greater than average
print("Marks greater than average:")

for mark in marks:
    if mark > average:
        print(mark)