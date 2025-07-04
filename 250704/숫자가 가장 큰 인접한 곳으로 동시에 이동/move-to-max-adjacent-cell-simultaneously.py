from collections import Counter

# N 격자, M 구슬 갯수, T 시간 
n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]

def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n

# 이동 우선순위 반영 (가장 큰 값 중 상→하→좌→우 순)
def simulation(r, c):
    drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우
    max_val = a[r-1][c-1]

    # 인접 칸 중 가장 큰 숫자 구하기
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if in_range(nr, nc):
            max_val = max(max_val, a[nr-1][nc-1])

    # 우선순위에 따라 가장 큰 숫자 칸으로 이동
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if in_range(nr, nc) and a[nr-1][nc-1] == max_val and a[nr-1][nc-1] > a[r-1][c-1]:
            return (nr, nc)

    return (r, c)

# 중복 확인
def check_duplicate(marbles):
    is_duplicate = [False] * len(marbles)
    for i in range(len(marbles)):
        for j in range(i+1, len(marbles)):
            if marbles[i] == marbles[j]:
                is_duplicate[i] = True
                is_duplicate[j] = True
    return is_duplicate

# 중복 제거
def delete_duplicate(marbles):
    # is_duplicate = check_duplicate(marbles)
    # return [marbles[i] for i in range(len(marbles)) if not is_duplicate[i]]
    count = Counter(marbles)
    return [pos for pos in marbles if count[pos] == 1]

# 시뮬레이션 T초 진행
for _ in range(t):
    next_marbles = []
    for r, c in marbles:
        next_marbles.append(simulation(r, c))
    marbles = delete_duplicate(next_marbles)

# 결과 출력
print(len(marbles))
