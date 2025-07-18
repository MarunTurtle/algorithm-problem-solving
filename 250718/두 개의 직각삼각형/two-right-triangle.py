n = int(input())

for i in range(n, 0, -1):
    for _ in range(i):
        print('*', end="")

    for _ in range((n - i) * 2):
        print(' ', end="")

    for _ in range(i):
        print('*', end="")
    print()

