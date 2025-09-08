board = [list(input()) for _ in range(10)]

for i in range(10):
    for j in range(10):
        if board[i][j] == 'B':
            b = [i, j]
        elif board[i][j] == 'R':
            r = [i, j]
        elif board[i][j] == 'L':
            l = [i, j]

print(abs(b[0] - l[0]) + abs(b[1] - l[1]) - 1)