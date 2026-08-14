class StudentProfile:
    def __init__(
        self,
        student_id,
        name,
        course,
        score,
        skills,
        is_placed
    ):
        # Store all received values in instance attributes
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.skills = skills
        self.is_placed = is_placed


student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
skills_input = input().strip()
placement_input = input().strip()

# Convert skills_input into a list of skill names
skills = skills_input.split(",")

skills = [skill.strip() for skill in skills]

# Convert placement_input into a Boolean value
if placement_input.lower() == "yes":
    is_placed = True
else:
    is_placed = False

# Create one StudentProfile object
student = StudentProfile(student_id, name, course, score, skills, is_placed)

# Print the stored student details
print("Student ID:", student.student_id)
print("Name:", student.name)
print("Course:", student.course)
print("Score:", student.score)
print(f"Skills: {', '.join(student.skills)}")

if is_placed == True:
    print("Placement Status: Placed")
else:
    print("Placement Status: Not Placed")