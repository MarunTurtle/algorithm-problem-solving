# N번의 턴, M개의 지점, K개의 말
N, M, K = map(int, input().split())
# 명령들
orders = list(map(int, input().split()))

total = 0
moves = [[1] for _ in range(K)]

def pos(i):
    return sum(moves[i])

def calc():
    return sum(1 for i in range(K) if pos(i) >= M )

def backtrack(turn):
    global total 

    if turn == N:
        total = max(total, calc())
        return
    
    for i in range(K):
        if moves[i] >= M:
            continue
        moves[i].append(orders[turn])
        backtrack(turn+1)
        moves[i].pop()
    
    backtrack(turn+1)

backtrack(0)
print(total)