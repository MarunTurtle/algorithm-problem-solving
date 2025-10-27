n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = float('inf')
selected = []
visited = [False] * (n+1)

def get_sum():
    return sum(selected)

def get_max_sum_combo(depth):
    global ans
    if depth == n:
        ans = min(ans, get_sum())
        return
    
    for i in range(n):
        if not visited[i] and depth != i:
            selected.append(grid[depth][i])
            visited[i] = True
            get_max_sum_combo(depth + 1)
            visited[i] = False
            selected.pop()

get_max_sum_combo(0)
print(ans)
