n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
x, y, = 0, 0
dxys = {"S": (0, -1), "N": (0, 1),  "W": (-1, 0), "E": (1, 0)}

for i in range(n):
    for j in range(dist[i]):
        dx, dy = dxys[dir[i]]
        x += dx
        y += dy

print(x, y)