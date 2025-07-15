n = int(input())

for i in range(n):
    row = []

    for j in range(n):
        row.append(j+1)
    
    if i % 2 != 0:
        row.reverse()
    
    for num in row:
        print(num, end="")
    print()


