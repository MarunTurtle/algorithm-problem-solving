n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
x, y = 0, 0

dx = {'E': 1, 'S': 0, 'W': -1, 'N': 0}
dy = {'E': 0, 'S': -1, 'W': 0, 'N': 1}

for i in range(n):
    for _ in range(dist[i]):
        nx = x + dx[dir[i]]
        ny = y + dy[dir[i]]
        x = nx
        y = ny

print(x, y)