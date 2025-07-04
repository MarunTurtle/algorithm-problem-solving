# 변수 선언 및 입력
n, m, t = tuple(map(int, input().split()))
a = [[0] * (n + 1)]
for _ in range(n):
    a.append([0] + list(map(int, input().split())))

count = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]
next_count = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]


# 범위가 격자 안에 들어가는지 확인합니다.
def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n


# 인접한 곳들 중 가장 값이 큰 위치를 반환합니다.
def get_max_neighbor_pos(curr_x, curr_y):
    # 코딩의 간결함을 위해 
    # 문제 조건에 맞게 상하좌우 순서로
    # 방향을 정의합니다.
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    max_num, max_pos = 0, (0, 0)
    
    # 각각의 방향에 대해 나아갈 수 있는 곳이 있는지 확인합니다.
    for dx, dy in zip(dxs, dys):
        next_x, next_y = curr_x + dx, curr_y + dy
        
        # 범위안에 들어오는 격자 중 최댓값을 갱신합니다.
        if in_range(next_x, next_y) and a[next_x][next_y] > max_num:
            max_num = a[next_x][next_y]
            max_pos = (next_x, next_y)
    
    return max_pos


# (x, y) 위치에 있는 구슬을 움직입니다.
def move(x, y):
    # 인접한 곳들 중 가장 값이 큰 위치를 계산합니다.
    next_x, next_y = get_max_neighbor_pos(x, y)
    
    # 그 다음 위치에 구슬의 개수를 1만큼 추가해줍니다.
    next_count[next_x][next_y] += 1


# 구슬을 전부 한 번씩 움직여 봅니다.
def move_all():
    # 그 다음 각 위치에서의 구슬 개수를 전부 초기화해놓습니다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            next_count[i][j] = 0
            
    # (i, j) 위치에 구슬이 있는경우 
    # 움직임을 시도해보고, 그 결과를 전부 next_count에 기록합니다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if count[i][j] == 1:
                move(i, j)
    
    # next_count 값을 count에 복사합니다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            count[i][j] = next_count[i][j]


# 충돌이 일어나는 구슬은 전부 지워줍니다.
def remove_duplicate_marbles():
    # 충돌이 일어난 구슬들이 있는 위치만 빈 곳으로 설정하면 됩니다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if count[i][j] >= 2:
                count[i][j] = 0


# 조건에 맞춰 시뮬레이션을 진행합니다.
def simulate():
    # Step1
    # 구슬을 전부 한 번씩 움직여 봅니다.
    move_all()
    
    # Step2
    # 움직임 이후에 충돌이 일어나는 구슬들을 골라 목록에서 지워줍니다.
    remove_duplicate_marbles()

        
# 초기 count 배열을 설정합니다.
# 구슬이 있는 곳에 1을 표시합니다.
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    count[x][y] = 1
    
# t초 동안 시뮬레이션을 진행합니다.
for _ in range(t):
    simulate()

# 출력:
ans = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        ans += count[i][j]

print(ans)