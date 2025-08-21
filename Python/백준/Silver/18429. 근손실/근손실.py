import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

visited = [False] * N

def dfs(day: int, cur: int) -> int:
    if day == N:
        return 1  
    total = 0
    for i in range(N):
        if not visited[i]:
            nxt = cur + A[i] - K
            if nxt >= 500:        
                visited[i] = True
                total += dfs(day + 1, nxt)
                visited[i] = False
    return total

print(dfs(0, 500))
