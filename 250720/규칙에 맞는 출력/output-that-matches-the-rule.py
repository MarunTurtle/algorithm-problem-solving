n = int(input())

for i in range(1, n+1):
    a = n - i + 1
    for j in range(i):   
        print(a, end=" ")
        a += 1
    print()
