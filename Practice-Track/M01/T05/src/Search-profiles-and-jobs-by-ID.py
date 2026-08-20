class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


class JobDescription:
    def __init__(self, job_id, company, role):
        self.job_id = job_id
        self.company = company
        self.role = role

    def __str__(self):
        return f"{self.job_id} - {self.company} - {self.role}"


class PlacementManager:
    def __init__(self):
        self.student_profiles = []
        self.job_descriptions = []

    def add_student_profile(self, student_profile):
        self.student_profiles.append(student_profile)

    def add_job_description(self, job_description):
        self.job_descriptions.append(job_description)

    def find_student_by_id(self, student_id):
        # Return the matching student object or None
        for student in self.student_profiles:
            if student.student_id == student_id:
                return student

        return False

    def find_job_by_id(self, job_id):
        # Return the matching job object or None
        for job in self.job_descriptions:
            if job.job_id == job_id:
                return job

        return False


manager = PlacementManager()

student_count = int(input())

for _ in range(student_count):
    student_id = int(input())
    name = input().strip()
    course = input().strip()

    student = StudentProfile(student_id, name, course)
    manager.add_student_profile(student)

job_count = int(input())

for _ in range(job_count):
    job_id = int(input())
    company = input().strip()
    role = input().strip()

    job = JobDescription(job_id, company, role)
    manager.add_job_description(job)

student_id_to_find = int(input())
job_id_to_find = int(input())

# Search for the student and job
student1 = manager.find_student_by_id(student_id_to_find)

if student1:
    print(f"Student Found: {student1}")
else:
    print("Student Not Found")

# Display the search results
job1 = manager.find_job_by_id(job_id_to_find)

if job1:
    print(f"Job Found: {job1}")
else:
    print("Job Not Found")