OFFSET = 100
MAX_R = 200

n = int(input())
checked = [0] * (MAX_R + 1)

for + in range(n):
    a, b = tuple(map(int, input().split()))
    a += OFFSET
    b += OFFSET
    for j in range(a, b):
        checked[j] += 1

print(max(checked))