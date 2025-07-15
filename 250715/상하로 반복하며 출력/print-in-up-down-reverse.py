n = int(input())

grid = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            grid[j][i] = j + 1
        else:
            grid[j][i] = n - j

for row in grid:
    for num in row:
        print(num, end="")
    print()

        
