class StudentProfile:
    pass

name = input().strip()

# Create an StudentProfile object
student = StudentProfile()

# Store the name in the object
student.name = name

# Print the stored name
print("Student Name:",student.name)