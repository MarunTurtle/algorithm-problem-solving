n = int(input())

for i in range(n):
    for _ in range(i + 1):
        print('*', end=" ")
    
    print()

    for _ in range(n - i):
        print('*', end=" ")
    
    print()