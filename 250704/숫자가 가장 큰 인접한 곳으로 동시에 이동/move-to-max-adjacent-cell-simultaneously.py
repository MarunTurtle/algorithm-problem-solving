# 상하좌우 이동
drs = [-1, 1, 0, 0]
dcs = [0, 0, -1, 1]

def in_range(n, r, c):
    return 0 <= r < n and 0 <= c < n

def simulate(n, m, t, grid, marbles):
    count = [[0] * n for _ in range(n)]
    
    # 초기 구슬 위치 설정
    for r, c in marbles:
        count[r][c] += 1

    for _ in range(t):
        next_count = [[0] * n for _ in range(n)]
        
        for r in range(n):
            for c in range(n):
                if count[r][c] > 0:
                    max_val = grid[r][c]
                    next_pos = (r, c)
                    for dir in range(4):
                        nr, nc = r + drs[dir], c + dcs[dir]
                        if in_range(n, nr, nc) and grid[nr][nc] > max_val:
                            max_val = grid[nr][nc]
                            next_pos = (nr, nc)
                    next_count[next_pos[0]][next_pos[1]] += count[r][c]
        
        # 충돌 처리
        for r in range(n):
            for c in range(n):
                if next_count[r][c] >= 2:
                    next_count[r][c] = 0
        count = next_count

    # 살아남은 구슬 수 세기
    return sum(count[r][c] for r in range(n) for c in range(n))

# 입력 받기
n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
marbles = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(m)]  # 0-indexed로 변환

# 결과 출력
print(simulate(n, m, t, grid, marbles))
