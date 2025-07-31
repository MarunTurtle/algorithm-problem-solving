n, m, k = map(int, input().split())

student_pts = [0] * (n + 1)

while True:
    x = int(input())
    student_pts[x] += 1
    if student_pts[x] >= k:
        print(x)
        break
    m -= 1
    if m == 0:
        print(-1)
        break
