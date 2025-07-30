MAX_K = 100000

w, b = 0, 0

checked = [0] * (2 * MAX_K + 1)

cur = MAX_K

n = int(input())

for i in range(n):
    x, direction = tuple(input().split())
    x = int(x)

    if direction == 'L':
        for i in range(x):
            checked[cur - i] = 1
        cur = cur - x + 1
    else: 
        for i in range(x):
            checked[cur + i] = 2
        cur = cur + x - 1

for i in range(2 * MAX_K + 1):
    if checked[i] == 1:
        w += 1
    elif checked[i] == 2:
        b += 1

print(w, b)