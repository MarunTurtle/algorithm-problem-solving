# N번의 턴, M개의 지점, K개의 말
N, M, K = map(int, input().split())
# 명령들
orders = list(map(int, input().split()))
total = 0
moves = [1 for _ in range(K)]

def calc():
    score = 0
    for move in moves:
        score += (move >= M)
    return score

def backtrack(turn):
    global total 

    total = max(total, calc())

    if turn == N:
        return
    
    for i in range(K):
        if moves[i] >= M:
            continue
        moves[i] += orders[turn]
        backtrack(turn+1)
        moves[i] -= orders[turn]

backtrack(0)
print(total)