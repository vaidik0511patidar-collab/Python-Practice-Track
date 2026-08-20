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
        self.skills = list(skills)
        self.is_placed = is_placed


class JobDescription:
    def __init__(
        self,
        job_id,
        company,
        role,
        location="Remote",
        minimum_score=0.0,
        required_skills=None,
        is_active=True
    ):
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.minimum_score = minimum_score
        self.required_skills = (
            []
            if required_skills is None
            else list(required_skills)
        )
        self.is_active = is_active


class PlacementManager:
    def __init__(self):
        # Create separate empty collections for students and jobs
        self.student_profiles = []
        self.job_descriptions = []


student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
skills_input = input().strip()
placement_input = input().strip()

job_id = int(input())
company = input().strip()
role = input().strip()
location = input().strip()
minimum_score = float(input())
required_skills_input = input().strip()
job_status_input = input().strip()


skills = [
    skill.strip()
    for skill in skills_input.split(",")
    if skill.strip()
]

required_skills = [
    skill.strip()
    for skill in required_skills_input.split(",")
    if skill.strip()
]


is_placed = placement_input.lower() == "yes"

is_active = job_status_input.lower() == "yes"


student = StudentProfile(
    student_id,
    name,
    course,
    score,
    skills,
    is_placed
)

job = JobDescription(
    job_id,
    company,
    role,
    location,
    minimum_score,
    required_skills,
    is_active
)

# Create exactly one PlacementManager object
manager = PlacementManager()

# Store the complete student and job objects
manager.student_profiles.append(student)
manager.job_descriptions.append(job)

# Print the collection sizes and stored-record summaries
print(f"Student Profiles: {len(manager.student_profiles)}")
print(f"Job Descriptions: {len(manager.job_descriptions)}")
print(f"Stored Student: {student.student_id} - {student.name}")
print(f"Stored Job: {job.job_id} - {job.role}")