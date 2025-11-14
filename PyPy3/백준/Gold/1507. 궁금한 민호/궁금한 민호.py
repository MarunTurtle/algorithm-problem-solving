import sys
input = sys.stdin.readline

n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]

# 일단 모든 간선이 필요하다고 가정
need = [[True] * n for _ in range(n)]

# 플로이드-와샬 역이용
for k in range(n):
    for i in range(n):
        if i == k:
            continue
        for j in range(n):
            if j == k or i == j:
                continue

            # 모순 체크: 더 짧은 경로가 존재한다면 이미 잘못된 표
            if dist[i][j] > dist[i][k] + dist[k][j]:
                print(-1)
                sys.exit(0)

            # 굳이 직접 도로가 필요 없는 경우 (i -> k -> j로 최단 거리 나오는 경우)
            if dist[i][j] == dist[i][k] + dist[k][j]:
                need[i][j] = False
                need[j][i] = False

# 필요한 도로들만 더함 (i < j만)
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if need[i][j]:
            ans += dist[i][j]

print(ans)
