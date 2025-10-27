n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = float('inf')
visited = [0] * (n)
visited[0] = True

def get_min_path(depth, cur, cost):
    global ans
    
    if cost >= ans:
        return

    if depth == n - 1:
        if grid[cur][0] > 0:
            ans = min(ans, cost + grid[cur][0])
        return

    for nxt in range(1, n):
        if not visited[nxt] and grid[cur][nxt] > 0 and nxt != cur:
            visited[nxt] = True
            get_min_path(depth + 1, nxt, cost + grid[cur][nxt])
            visited[nxt] = False

get_min_path(0, 0, 0)
print(ans)