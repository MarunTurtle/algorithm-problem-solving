n = int(input())

students = [(*map(int, input().split()), i+1) for i in range(n)]
students.sort(key=lambda x:(x[0], -x[1]))

for student in students:
    print(*student)

