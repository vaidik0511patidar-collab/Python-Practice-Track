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
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.skills = skills
        self.is_placed = is_placed

    def __str__(self):
        # Return the complete formatted student profile
        status = "Placed" if self.is_placed else "Not Placed"

        return f"Student ID: {self.student_id}\nName: {self.name}\nCourse: {self.course}\nScore: {self.score:.1f}\nSkills: {(', ').join(self.skills)}\nPlacement Status: {status}"

student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
skills_input = input().strip()
placement_input = input().strip()

skills = [
    skill.strip()
    for skill in skills_input.split(",")
    if skill.strip()
]

is_placed = placement_input.lower() == "yes"

# Create one StudentProfile object
student = StudentProfile(student_id, name, course, score, skills, is_placed)

# Display the object using print(student)
print(student)