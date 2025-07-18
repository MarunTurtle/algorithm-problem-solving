n = int(input())

# n -> 1 
# n * 2 - 1

for i in range(n, 0, -1):
    for _ in range(n - i):
        print(' ', end=" ")
    
    for _ in range(2 * i - 1):
        print('*', end=" ")
    print()