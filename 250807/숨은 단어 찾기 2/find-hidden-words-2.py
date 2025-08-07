n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

ans = 0

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

for i in range(n):
    for j in range(m):
        if board[i][j] != 'L':
            continue
        else:
            for d in range(8):
                nr, nc = i, j
                cnt = 0
                for k in range(2):
                    nr += dx[d]
                    nc += dy[d]
                    if not in_range(nr, nc):
                        break
                    if board[nr][nc] != 'E':
                        break
                    cnt += 1
                if cnt == 2:
                    ans += 1

print(ans)