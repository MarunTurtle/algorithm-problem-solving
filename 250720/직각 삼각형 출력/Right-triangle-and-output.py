n = int(input())

for i in range(n):
    for j in range(i * 2 + 1):
        print('*', end="")
    print()