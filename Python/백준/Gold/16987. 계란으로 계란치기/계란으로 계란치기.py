import sys
input = sys.stdin.readline

N = int(input().strip())
eggs = [list(map(int, input().split())) for _ in range(N)]

ans = 0

def dfs(idx):
    global ans

    if idx == N:  # 모든 계란을 다 들었음
        broken = sum(1 for s, _ in eggs if s <= 0)
        ans = max(ans, broken)
        return

    if eggs[idx][0] <= 0:  # 손에 든 계란이 이미 깨졌으면
        dfs(idx + 1)
        return

    hit = False
    for j in range(N):
        if j == idx or eggs[j][0] <= 0:  # 자기 자신이거나 이미 깨진 계란
            continue
        # 계란 idx와 j 충돌
        eggs[idx][0] -= eggs[j][1]
        eggs[j][0] -= eggs[idx][1]
        hit = True

        dfs(idx + 1)

        # 원상복구
        eggs[idx][0] += eggs[j][1]
        eggs[j][0] += eggs[idx][1]

    if not hit:  # 칠 수 있는 계란이 하나도 없으면 그냥 넘김
        dfs(idx + 1)


dfs(0)
print(ans)
