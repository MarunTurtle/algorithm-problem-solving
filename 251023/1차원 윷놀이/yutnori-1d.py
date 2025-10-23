# N번의 턴, M개의 지점, K개의 말
N, M, K = map(int, input().split())
orders = list(map(int, input().split()))

total = 0
pos = [1] * K  # 각 말의 현재 위치(1부터 시작)

def backtrack(turn: int, finished: int):
    global total

    # 상한 계산으로 가지치기
    remain = N - turn
    unfinished = sum(1 for x in pos if x < M)
    ub = finished + min(remain, unfinished)
    if ub <= total:
        return

    if turn == N:
        if finished > total:
            total = finished
        return

    step = orders[turn]

    # 이번 턴에 움직일 수 있는 말을 하나 선택해서 진행
    moved_any = False
    for i in range(K):
        if pos[i] >= M:          # 이미 완주한 말은 스킵
            continue
        moved_any = True

        before = pos[i]
        pos[i] += step

        # 이번 이동으로 새로 완주했는지 체크
        gained = 1 if before < M and pos[i] >= M else 0
        backtrack(turn + 1, finished + gained)

        pos[i] = before  # 복원

    # 만약 모든 말이 이미 완주해서 아무도 못 움직이면 턴만 소모
    if not moved_any:
        backtrack(turn + 1, finished)

backtrack(0, 0)
print(total)
