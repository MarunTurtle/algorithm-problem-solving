from collections import deque

# 입력 받기
grid = [list(input()) for _ in range(10)]

# 시작점(L), 도착점(B) 찾기
for i in range(10):
    for j in range(10):
        if grid[i][j] == 'L':
            start = (i, j)
        elif grid[i][j] == 'B':
            end = (i, j)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 여부 및 거리 저장 배열
visited = [[False] * 10 for _ in range(10)]
distance = [[0] * 10 for _ in range(10)]

# BFS 시작
queue = deque()
queue.append(start)
visited[start[0]][start[1]] = True

while queue:
    x, y = queue.popleft()

    # 도착점에 도달하면 종료
    if (x, y) == end:
        print(distance[x][y]-1)
        break

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < 10 and 0 <= ny < 10:
            if not visited[nx][ny] and grid[nx][ny] != 'R':
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
