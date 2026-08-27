class JobOpening:
    def __init__(self, role, minimum_salary, maximum_salary):
        self.role = role
        self.__minimum_salary = minimum_salary
        self.__maximum_salary = maximum_salary

    @property
    def minimum_salary(self):
        return self.__minimum_salary

    @property
    def maximum_salary(self):
        return self.__maximum_salary

    def update_salary_range(self, new_minimum, new_maximum):
        if new_minimum >= 0 and new_maximum >= 0:
            if new_minimum <= new_maximum:
                self.__minimum_salary = new_minimum
                self.__maximum_salary = new_maximum


role = input().strip()
minimum_salary = int(input())
maximum_salary = int(input())
new_minimum = int(input())
new_maximum = int(input())

job = JobOpening(role, minimum_salary, maximum_salary)
job.update_salary_range(new_minimum, new_maximum)

print(f"Role: {job.role}")
print(f"Salary Range: {job.minimum_salary} - {job.maximum_salary}")