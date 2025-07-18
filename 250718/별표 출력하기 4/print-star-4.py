n = int(input())

for i in range(n):
    for j in range(n - i):
        print('*', end=" ")
    print()

for k in range(2, n+1):
    for l in range(k):
        print('*', end=" ")
    print()
