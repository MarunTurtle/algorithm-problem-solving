n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

sum_list = [[0] * (n-2) for _ in range(n)]

for i in range(n):
    for j in range(n-2):
        sum_list[i][j] = grid[i][j] + grid[i][j+1] + grid[i][j+2]
    
ans = -1

for i in range(n):
    for j in range(n-2):
        for k in range(n):
            for l in range(n-2):
                if i == k and abs(j - 1) <= 2:
                    continue
                
                first = sum_list[i][j]
                second = sum_list[k][l]
                ans = max(ans, first+second)

print(ans)
