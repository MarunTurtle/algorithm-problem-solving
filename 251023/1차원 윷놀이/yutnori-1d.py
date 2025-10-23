# N번의 턴, M개의 지점, K개의 말
N, M, K = map(int, input().split())
orders = list(map(int, input().split()))

total = 0
moves = [1] * K  # 각 말의 현재 위치(시작이 1이라 가정)

def calc():
    return sum(1 for x in moves if x >= M)

def backtrack(turn):
    global total
    if turn == N:
        total = max(total, calc())
        return

    step = orders[turn]
    for i in range(K):
        if moves[i] >= M:      # 이미 도착한 말은 건너뜀
            continue
        moves[i] += step       # i번 말을 이번 턴에 이동
        backtrack(turn + 1)    # 다음 턴으로
        moves[i] -= step       # 원상복구

backtrack(0)
print(total)
