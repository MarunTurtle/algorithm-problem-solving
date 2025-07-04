# 변수 선언 및 입력
n, r, c = map(int, input().split())
a = [[0] * (n + 1)]
for _ in range(n):
    a.append([0] + list(map(int, input().split())))

# 방문하게 되는 숫자들을 담을 곳입니다.
visited_nums = []

# 범위가 격자 안에 들어가는지 확인합니다. 
def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n

# 범위가 격자 안이고, 해당 위치의 값이 더 큰지 확인합니다. 
def can_go(x, y, curr_num):
    return in_range(x, y) and a[x][y] > curr_num

# 조건에 맞춰 움직여봅니다. 
# 움직였다면 true를 반환하고
# 만약 움직일 수 있는 곳이 없었다면 false를 반환합니다. 
def simulate():
    global r, c

    drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc

        if can_go(nr, nc, a[r][c]):
            r, c = nr, nc
            return True

    return False

# 초기 위치를 방문 위치에 추가
visited_nums.append(a[r][c])

while True:
    # 조건에 맞춰 움직여 봅니다. 
    greater_number_exist = simulate()
    # 인접한 곳에 더 큰 숫자가 없다면 종료
    if not greater_number_exist:
        break
    # 움직이고 난 후의 위치를 방문 위치에 넣기
    visited_nums.append(a[r][c])

# 출력
print(*visited_nums)