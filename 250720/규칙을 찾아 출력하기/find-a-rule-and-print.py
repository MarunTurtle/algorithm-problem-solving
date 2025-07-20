n = int(input())

for i in range(n):
    if i == 0:
        for j in range(n):
            print('*', end=" ")    
    else:
        for j in range(i):
            print('*', end=" ")
        
        for j in range(n - i - 1):
            print(" ", end=" ")
        print('*', end="")
    print()
