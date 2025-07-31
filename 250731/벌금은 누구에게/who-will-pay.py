n, m, k = map(int, input().split())

student_pts = [0] * (n + 1)

ans = -1

for i in range(m):
    x = int(input())
    student_pts[x] += 1
    
    if student_pts[x] >= k:
        ans = x
        break
        
print(ans)
