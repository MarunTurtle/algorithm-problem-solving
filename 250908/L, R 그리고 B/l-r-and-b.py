board = [list(input()) for _ in range(10)]

for i in range(10):
    for j in range(10):
        if board[i][j] == 'B':
            b = tuple(i, j)
        elif board[i][j] == 'R':
            r = tupel(i, j)
        elif board[i][j] == 'L':
            l = tuple(i, j)

print(1 + b[0] - l[0] + b[1] - l[1])