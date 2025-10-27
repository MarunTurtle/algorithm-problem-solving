n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = float('inf')
picked = []
visited = [0] * (n)

def get_min_path(depth):
    global ans

    if depth == n: 
        ans = min(ans, sum(picked))
        print(picked)
        return

    for row in range(n):
        if grid[row][depth] == 0:
            continue
        if not visited[row]:
            picked.append(grid[row][depth])
            visited[row] = True
            get_min_path(depth + 1)
            visited[row] = False
            picked.pop()

get_min_path(0)
print(ans)