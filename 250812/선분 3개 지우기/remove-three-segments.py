n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
count = 0

for i in range(n-1):
    for j in range(i+1, n):
        x1, x2 = lines[i]
        x3, x4 = lines[j]
        
        if x1 < x4 and x2 < x3:
            count += 1
        elif x3 < x2 and x4 < x1:
            count += 1

print(count)