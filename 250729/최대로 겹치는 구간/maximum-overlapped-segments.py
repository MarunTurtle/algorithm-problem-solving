n = int(input())
dots = [0] * 201

for i in range(n):
    a, b = tuple(map(int, input().split()))
    a += 100
    b += 100
    for j in range(a, b+1):
        dots[j] += 1

print(max(dots))
