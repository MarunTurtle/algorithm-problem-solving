# N번의 턴, M개의 지점, K개의 말
N, M, K = map(int, input().split())
orders = list(map(int, input().split()))

total = 0
moves = [[1] for _ in range(K)]  # 각 말의 진행 경로(1 + 배정된 이동량들)

def pos(i):
    return sum(moves[i])  # i번 말 현재 위치

def calc():
    # 도착한 말 수
    return sum(1 for i in range(K) if pos(i) >= M)

def backtrack(turn):
    global total
    if turn == N:
        total = max(total, calc())
        return

    step = orders[turn]
    moved_any = False

    # 이번 턴에 움직일 수 있는 말 하나를 골라 이동
    for i in range(K):
        if pos(i) >= M:   # 이미 도착한 말은 건너뜀
            continue
        moved_any = True
        moves[i].append(step)
        backtrack(turn + 1)
        moves[i].pop()

    # 스킵이 허용된다면 유지, 불가라면 이 블록 삭제
    if not moved_any:
        # 모든 말이 이미 도착해도 턴은 진행
        backtrack(turn + 1)

backtrack(0)
print(total)
