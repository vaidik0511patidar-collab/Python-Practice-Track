class StudentProfile:
    # Add the constructor and properties here
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    @property
    def name(self):
        return self.__name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,new_score):
        self.__score = new_score

name = input().strip()
score = int(input())
new_score = int(input())

student = StudentProfile(name,score)
student.score = new_score

print(f"Student Name: {student.name}")
print(f"Student Score: {student.score}")