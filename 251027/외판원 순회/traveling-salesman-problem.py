n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = float('inf')
selected = []
visited = [False] * (n+1)

def get_sum():
    return sum(selected)

def no_zero():
    for num in selected:
        if num == 0:
            return False
    return True

def get_min_sum_combo(depth):
    global ans
    if depth == n:
        if no_zero():
            ans = min(ans, get_sum())
            return
        return
    
    for i in range(n):
        if depth != i and not visited[i]:           
            selected.append(grid[depth][i])
            visited[i] = True
            get_min_sum_combo(depth + 1)
            visited[i] = False
            selected.pop()

get_min_sum_combo(0)
print(ans)
