n = int(input())

for i in range(n): # i: 0 - > n
    for _ in range(n - i - 1):
        print(' ', end=" ")

    for _ in range(i + 1):
        print('@', end=" ")

    print()
    
for i in range(n-1, 0, -1):
    for _ in range(i):
        print('@', end=" ")
    print()