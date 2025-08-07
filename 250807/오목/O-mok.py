board = [[0] * 20] + [[0] + list(map(int, input().split())) for _ in range(19)]
dx = [0, 1, 1, -1]
dy = [1, 1, 0, 1]

def in_range(x, y):
    return 1 <= x < 20 and 1 <= y < 20

black_win = None  # (i, j) 저장용
white_win = None

for i in range(1, 20):
    for j in range(1, 20):
        if board[i][j] == 0:
            continue
        color = board[i][j]
        for d in range(4):
            cnt = 1
            x, y = i, j
            for _ in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if not in_range(nx, ny) or board[nx][ny] != color:
                    break
                cnt += 1
                x, y = nx, ny
            if cnt == 5:
                if color == 1 and black_win is None:
                    black_win = (i + (dx[d] * 2), j + (dy[d] * 2))
                elif color == 2 and white_win is None:
                    white_win = (i + (dx[d] * 2), j + (dy[d] * 2))

# 탐색 끝난 뒤 결과 판단
if black_win and white_win:
    print(0)
elif black_win:
    print(1)
    print(black_win[0], black_win[1])
elif white_win:
    print(2)
    print(white_win[0], white_win[1])
else:
    print(0)