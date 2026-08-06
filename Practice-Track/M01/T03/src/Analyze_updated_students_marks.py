student_count = int(input())
marks = []

# Read and store all the marks using append()
for i in range(student_count):
    mark = int(input())
    marks.append(mark)

position = int(input())
corrected_mark = int(input())
passing_mark = int(input())

# Update the mark at entered student position
marks.pop(position-1)
marks.insert(position-1,corrected_mark)

# Calculate the total, highest, lowest and average marks
total = sum(marks)
highest = max(marks)
lowest = min(marks)
average = total/student_count

passed_students = 0

# Count the students whose marks satisfy the passing condition
for i in marks:
    if i >= passing_mark:
        passed_students += 1

# Display the final analysis
print(f"Updated Marks: {marks}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Highest Mark: {highest}")
print(f"Lowest Mark: {lowest}")
print(f"Passed Students: {passed_students}")