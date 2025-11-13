import sys
input = sys.stdin.readline

DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # 위, 아래, 오른쪽, 왼쪽

def move_shark():
    new_fishing_spot = [[-1] * C for _ in range(R)]

    for m in range(M):
        if dead_sharks[m]:
            continue

        shark_r, shark_c, shark_s, shark_d, shark_z = sharks_info[m]

        if shark_d in (0, 1):  # 세로 이동
            
            dr = DIRECTIONS[shark_d][0]
            nr = (shark_r + dr * shark_s) % R2
            if nr > R - 1:
                nr = R2 - nr
                shark_d ^= 1  # 0<->1 반전

            nc = shark_c  # 열은 그대로

        else:              # 가로 이동
            if C2:  # C > 1
                dc = DIRECTIONS[shark_d][1]
                nc = (shark_c + dc * shark_s) % C2
                if nc > C - 1:
                    nc = C2 - nc
                    # 2<->3 반전: 2 + ((d-2) ^ 1)
                    shark_d = 2 + ((shark_d - 2) ^ 1)
            else:
                nc = 0  # C==1이면 열은 고정
            nr = shark_r  # 행은 그대로

        shark_r, shark_c = nr, nc
        sharks_info[m][0], sharks_info[m][1], sharks_info[m][3] = shark_r, shark_c, shark_d

        # 충돌 처리 (큰 상어만 생존)
        if new_fishing_spot[shark_r][shark_c] == -1:
            new_fishing_spot[shark_r][shark_c] = m
        else:
            other = new_fishing_spot[shark_r][shark_c]
            if shark_z > sharks_info[other][4]:
                new_fishing_spot[shark_r][shark_c] = m
                dead_sharks[other] = True
            else:
                dead_sharks[m] = True

    return new_fishing_spot


def fishing (y):
    x = 0

    while x < R:
        if fishing_spot[x][y] >= 0:
            sharks_num = fishing_spot[x][y]
            dead_sharks[sharks_num] = True
            return sharks_info[sharks_num][4]
        x += 1

    return 0


R, C, M = map(int, input().split())  # R: 행, C: 열, M: 상어의 수
fishing_spot = [[-1] * C for _ in range(R)]  # 상어의 인덱스 번호를 담을 배열
sharks_info = []   # (r, c): 상어의 위치, s: 속도, d: 진행 방향, z: 사이즈
R2 = 2 * (R - 1)
C2 = 2 * (C - 1)

dead_sharks = [False] * M
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks_info.append([r-1, c-1, s, d-1, z])
    fishing_spot[r-1][c-1] = i

total_size = 0
fishman_loc = 0

while fishman_loc < C:
    total_size += fishing(fishman_loc)
    fishing_spot = move_shark()
    fishman_loc += 1

print(total_size)

