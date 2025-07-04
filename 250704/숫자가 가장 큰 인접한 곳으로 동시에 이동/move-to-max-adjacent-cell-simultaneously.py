from collections import defaultdict

# 입력 받기
n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
marbles = [tuple(map(int, input().split())) for _ in range(m)]

# 상하좌우 방향 (우선순위: 상 > 하 > 좌 > 우)
drs = [-1, 1, 0, 0]
dcs = [0, 0, -1, 1]

# T초 동안 시뮬레이션 반복
for _ in range(t):
    # 다음 위치 저장용
    next_pos = defaultdict(int)
    move_list = []

    for r, c in marbles:
        max_val = grid[r - 1][c - 1]
        target = (r, c)  # 이동하지 않을 수도 있음

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if 1 <= nr <= n and 1 <= nc <= n:
                if grid[nr - 1][nc - 1] > max_val:
                    max_val = grid[nr - 1][nc - 1]
                    target = (nr, nc)

        move_list.append(target)
        next_pos[target] += 1

    # 한 칸에 여러 개 구슬 모이면 모두 제거
    marbles = [pos for pos in move_list if next_pos[pos] == 1]

# 결과 출력
print(len(marbles))
