n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = float('inf')
picked = []
visited = [0] * (n)

def get_min_path(depth, start):
    global ans
    if depth == n:
        if start == 0:     
            ans = min(ans, sum(picked))
            # if ans == sum(picked):
            #     print(picked)
        return

    for col in range(n):
        if grid[start][col] == 0:
            continue
        if not visited[col]:
            picked.append(grid[start][col])
            visited[col] = True
            get_min_path(depth + 1, col)
            visited[col] = False
            picked.pop()

get_min_path(0, 0)
print(ans)