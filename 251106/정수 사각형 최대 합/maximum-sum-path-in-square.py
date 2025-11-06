n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
score = [[0] * n for _ in range(n)]


def initialize():
    score[0][0] = grid[0][0]
    for i in range(1, n):
        score[i][0] = grid[i][0] + score[i-1][0] 
        score[0][i] = grid[0][i] + score[0][i-1]

initialize()

for i in range(1, n):
    for j in range(1, n):
        base = grid[i][j]
        top = score[i-1][j]
        left = score[i][j-1]

        score[i][j] = max(top, left) + base

print(score[n-1][n-1])

# for row in grid:
#     print(*row)

# print("-=-----")

# for row in score:
#     print(*row)