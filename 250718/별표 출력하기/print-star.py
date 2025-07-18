n = int(input())

for i in range(n):
    for j in range(i+1):
        print('*', end=" ")
    print()

for k in range(n-1, 0, -1):
    for l in range(k):
        print('*', end=" ")
    print()