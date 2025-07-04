# 상하좌우 (우선순위 순: 상, 하, 좌, 우)
drs = [-1, 1, 0, 0]
dcs = [0, 0, -1, 1]

def in_range(n, r, c):
    return 0 <= r < n and 0 <= c < n

def simulate(n, m, t, grid, marbles):
    count = [[0] * n for _ in range(n)]
    for r, c in marbles:
        count[r][c] += 1

    for _ in range(t):
        next_count = [[0] * n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if count[r][c] > 0:
                    max_val = grid[r][c]
                    candidates = [(r, c)]

                    for dir in range(4):
                        nr, nc = r + drs[dir], c + dcs[dir]
                        if in_range(n, nr, nc):
                            if grid[nr][nc] > max_val:
                                max_val = grid[nr][nc]
                                candidates = [(nr, nc)]
                            elif grid[nr][nc] == max_val:
                                candidates.append((nr, nc))

                    # 상하좌우 우선순위에 따라 정렬
                    move_r, move_c = sorted(candidates)[0]
                    next_count[move_r][move_c] += count[r][c]

        # 충돌 처리
        for r in range(n):
            for c in range(n):
                if next_count[r][c] >= 2:
                    next_count[r][c] = 0

        count = next_count

    return sum(count[r][c] for r in range(n) for c in range(n))

# 입력 받기
n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
marbles = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(m)]  # 0-indexed 변환

# 결과 출력
print(simulate(n, m, t, grid, marbles))
