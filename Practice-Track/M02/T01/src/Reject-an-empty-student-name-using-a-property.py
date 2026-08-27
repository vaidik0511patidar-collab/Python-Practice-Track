class StudentProfile:
    # Add the constructor and name property here
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        new_name = new_name.strip()
        
        if new_name != "":
            self.__name = new_name

initial_name = input()
new_name = input()

student = StudentProfile(initial_name)
student.name = new_name

print(f"Student Name: {student.name}")