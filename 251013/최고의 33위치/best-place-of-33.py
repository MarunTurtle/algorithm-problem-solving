n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_count = 0

for r in range(n-2):
    for c in range(n-2):
        count = 0
        for i in range(3):
            for j in range(3):
                if grid[r+i][c+j] == 1:
                    count += 1
        max_count = max(max_count, count)

print(max_count)