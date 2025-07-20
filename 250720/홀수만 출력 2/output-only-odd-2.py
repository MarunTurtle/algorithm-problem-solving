s, e = map(int, input().split())

for i in range(s, e-1, -1):
    if i % 2 == 1:
        print(i, end=" ")