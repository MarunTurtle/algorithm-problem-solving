import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input().strip())
S = [list(map(int, input().split())) for _ in range(N)]

# sym[i][j] = Sij + Sji (i<j만 사용)
sym = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        sym[i][j] = S[i][j] + S[j][i]

players = list(range(N))
half = N // 2

# 사람 0을 스타트 팀에 고정하여 대칭 제거
min_diff = float('inf')
for start_team_rest in combinations(range(1, N), half-1):
    start_team = (0,) + start_team_rest
    start_set = set(start_team)
    link_team = [p for p in players if p not in start_set]

    # 팀 점수 계산: i<j 쌍에 대한 sym 합
    start_score = 0
    for i in range(half):
        for j in range(i+1, half):
            a, b = start_team[i], start_team[j]
            if a < b:
                start_score += sym[a][b]
            else:
                start_score += sym[b][a]

    link_score = 0
    for i in range(half):
        for j in range(i+1, half):
            a, b = link_team[i], link_team[j]
            if a < b:
                link_score += sym[a][b]
            else:
                link_score += sym[b][a]

    diff = abs(start_score - link_score)
    if diff < min_diff:
        min_diff = diff
        if min_diff == 0:
            break

print(min_diff)
