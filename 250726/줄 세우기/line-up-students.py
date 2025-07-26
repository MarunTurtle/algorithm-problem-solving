class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number
        
n = int(input())
students = []

for i in range(1, n+1):
    height, weight = tuple(map(int, input().split()))
    number = i

    student = Student(height, weight, number)
    students.append(student)

students.sort(key=lambda x:(-x.height, -x.weight, x.number))

for idx, student in enumerate(students, start=1):
    print(f'{student.height} {student.weight} {student.number}')


