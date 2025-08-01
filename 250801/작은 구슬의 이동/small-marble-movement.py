n, t = map(int, input().split())
grid = [[0] * (n+1) for _ in range(n+1)]

dr = [0, -1, 1, 0]
dc = [1, 0, 0, -1]

dir_dict = {
    'U': 1,
    'D': 2,
    'L': 3,
    'R': 0
}

r, c, d = input().split()
r, c = int(r), int(c)
drct = dir_dict[d]
    
for i in range(t):
    nr = r + dr[drct]
    nc = c + dc[drct]

    if 1 <= nr <= n and 1 <= nc <= n:
        r, c = nr, nc
    else:
        drct = 3 - dir_dict[d]

print(r, c)