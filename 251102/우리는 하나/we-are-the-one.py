from collections import deque

# 변수 선언 및 입력
n, k, u, d = tuple(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0

s_pos = []
pos = [(i, j) for i in range(n) for j in range(n)]

# bfs에 필요한 변수들 입니다.
q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y, target):
    if not in_range(x, y) or visited[x][y]:
        return False
    
    diff = abs(target - a[x][y])
    return u <= diff and diff <= d

def bfs():
    while q:
        x, y = q.popleft()        
        dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, a[x][y]):
                q.append((nx, ny))
                visited[nx][ny] = True
                
def calc():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

    for x, y in s_pos:
        q.append((x, y))
        visited[x][y] = True
        
    bfs()
    
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1
                
    return cnt


def find_max(idx, cnt):
    global ans
    
    if cnt > k:
        return
    
    if idx == n * n:
        if cnt == k:
            ans = max(ans, calc())
        return
    
    s_pos.append(pos[idx])
    find_max(idx + 1, cnt + 1)
    s_pos.pop()
    
    find_max(idx + 1, cnt)


find_max(0, 0)
print(ans)
