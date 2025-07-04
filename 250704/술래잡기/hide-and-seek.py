# 격자에서 dx dy technique을 위한 util
# dxs, dys: 상, 우, 하, 좌
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 변수 선언 및 입력
n, m, h, k = map(int, input().split())


# 도망자의 이동을 관리하기 위한 배열을 정의
# hiders[i][j]: 격자 (i, j)에 위치한 도망자들의 방향 정보, 해당 위치에 도망자가 없다면 빈 배열
hiders = [
    [[] for _ in range(n)]
    for _ in range(n)
]

# 동시 이동을 위한 임시 배열
next_hiders = [
    [[] for _ in range(n)]
    for _ in range(n)
]

# 도망자 정보 입력
for _ in range(m):
    x, y, d = tuple(map(int, input().split()))
    hiders[x - 1][y - 1].append(d) # 0 based index 사용


# 나무의 정보 또한 위치를 통한 빠른 조회를 위해 2차원 배열로 관리
tree = [
    [False] * n
    for _ in range(n)
]

# 나무 정보 입력
for _ in range(h):
    x, y = tuple(map(int, input().split()))
    tree[x - 1][y - 1] = True # 0 based index 사용


def hider_move(x, y, move_dir):
    # 1. 술래와 거리가 3 초과 시 정지
    if abs(seeker_x - x) + abs(seeker_y - y) > 3:
        next_hiders[x][y].append(move_dir)
        return
    
    # 2. 방향에 따라 다음 위치 계산 및 벽 충돌 시 방향 전환
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if not in_range(nx, ny):
        # 상(0) <-> 하(2), 우(1) <-> 좌(3)
        move_dir = (move_dir + 2) % 4
        nx, ny = x + dxs[move_dir], y + dys[move_dir]

    # 3. 다음 위치에 술래가 없다면 이동, 있다면 정지
    if nx == seeker_x and ny == seeker_y:
        next_hiders[x][y].append(move_dir)
    else:
        next_hiders[nx][ny].append(move_dir)

def hider_moves():
    # 모든 도망자 이동 규칙 적용
    for i in range(n):
        for j in range(n):
            for hider_dir in hiders[i][j]:
                hider_move(i, j, hider_dir)

    # 임시 배열의 결과를 원래 배열로 복사
    # 임시 배열 초기화
    for i in range(n):
        for j in range(n):
            hiders[i][j] = next_hiders[i][j]
            next_hiders[i][j] = []

def seeker_move():
    global seeker_x, seeker_y, seeker_dir

    # 현재 방향으로 한 칸 이동
    seeker_x += dxs[seeker_dir]
    seeker_y += dys[seeker_dir]

    # x - y = -1 선상, x가 n//2 미만일때 위->오른쪽, 왼쪽->아래
    if seeker_x - seeker_y == -1 and seeker_x < n//2:
        if seeker_dir == 0:
            seeker_dir = 1
        elif seeker_dir == 3:
            seeker_dir = 2

    # x + y = n - 1 선상, x가 n//2 미만일때 오른쪽->아래, 위->왼쪽
    if seeker_x + seeker_y == n - 1 and seeker_x < n//2:
        if seeker_dir == 1:
            seeker_dir = 2
        elif seeker_dir == 0:
            seeker_dir = 3

    # x - y = 0 선상, x가 n//2 초과일때 아래->왼쪽, 오른쪽->위
    if seeker_x - seeker_y == 0 and seeker_x > n//2:
        if seeker_dir == 2:
            seeker_dir = 3
        elif seeker_dir == 1:
            seeker_dir = 0

    # x + y = n - 1 선상, x가 n//2 초과일때 왼쪽->위, 아래->오른쪽
    if seeker_x + seeker_y == n - 1 and seeker_x > n//2:
        if seeker_dir == 3:
            seeker_dir = 0
        elif seeker_dir == 2:
            seeker_dir = 1

    # (0, 0) 위를 바라볼때 아래방향
    if seeker_x == 0 and seeker_y == 0 and seeker_dir == 0:
        seeker_dir = 2

    # (n//2, n//2) 아래를 바라볼때 위방향
    if seeker_x == n//2 and seeker_y == n//2 and seeker_dir == 2:
        seeker_dir = 0

def catch_hiders(t):
    global score

    for dist in range(3):
        nx, ny = seeker_x + dist * dxs[seeker_dir], seeker_y + dist * dys[seeker_dir]

        # 격자 밖이거나, 나무가 있으면 넘어감
        if not in_range(nx, ny) or tree[nx][ny]:
            continue
        
        # 해당 위치의 도망자 수만큼 점수 획득
        score += t * len(hiders[nx][ny])
        # 해당 위치의 도망자는 맵에서 제거
        hiders[nx][ny] = []


# 술래의 위치 및 방향 초기화
seeker_x, seeker_y, seeker_dir = n//2, n//2, 0

# 점수를 계산하기 위한 변수 선언 및 초기화
score = 0

# 총 k번의 턴을 진행
# 각 턴은 도망자 움직임, 술래 움직임, 도망자 잡기 순서로 이루어짐
for t in range(1, k+1):
    # 1. 도망자 이동
    hider_moves()
    # 2. 술래 이동
    seeker_move()
    # 3. 도망자 잡기 및 점수 계산
    catch_hiders(t)

# 최종 점수 출력
print(score)