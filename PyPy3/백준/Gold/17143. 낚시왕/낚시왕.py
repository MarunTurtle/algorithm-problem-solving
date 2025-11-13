n, m, q = map(int, input().split())
ocean = [[0] * (m + 1) for _ in range(n + 1)]
sharks = []
# r, c, speed, direction, size
for _ in range(q):
    r, c, speed, dir, size = tuple(map(int, input().split()))
    shark = (r, c, speed, dir, size)
    sharks.append(shark)
    ocean[r][c] = shark

ans = 0

def in_range(r, c):
    return 1 <= r <= n and 1 <= c <= m

def catch_shark(idx):
    for row in range(1, n + 1):
        if ocean[row][idx] != 0:
            value = ocean[row][idx][4]
            caught_shark = ocean[row][idx]
            ocean[row][idx] = 0

            if caught_shark in sharks:
                sharks.remove(caught_shark)

            return value
    return 0

drs, dcs = [0, -1, 1, 0, 0], [0, 0, 0, 1, -1]

def change_dir(dir):
    if dir == 1:
        return 2
    elif dir == 2:
        return 1
    elif dir == 3:
        return 4
    else:
        return 3

def move(shark):
    r, c, speed, dir, size = shark

    if dir == 1 or dir == 2: 
        cycle = (n - 1) * 2
        if cycle != 0:
            s = speed % cycle
        else:
            s = 0
    else:  
        cycle = (m - 1) * 2
        if cycle != 0:
            s = speed % cycle
        else:
            s = 0

    dr, dc = drs[dir], dcs[dir]

    for _ in range(s):
        nr, nc = r + dr, c + dc
        if in_range(nr, nc):
            r, c = nr, nc
        else:
            dir = change_dir(dir)
            dr, dc = drs[dir], dcs[dir]
            r, c = r + dr, c + dc

    return (r, c, speed, dir, size)

def sharks_move():
    global ocean, sharks
    new_ocean = [[0] * (m + 1) for _ in range(n + 1)]

    for shark in sharks:
        nr, nc, s, d, z = move(shark)

        if new_ocean[nr][nc] == 0:
            new_ocean[nr][nc] = (nr, nc, s, d, z)
        else:
            if new_ocean[nr][nc][4] < z:
                new_ocean[nr][nc] = (nr, nc, s, d, z)

    new_sharks = []
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if new_ocean[r][c] != 0:
                new_sharks.append(new_ocean[r][c])

    sharks = new_sharks
    ocean = [row[:] for row in new_ocean]

for idx in range(1, m + 1):
    # print("=======")
    # for row in ocean:
    #     print(*row)

    ans += catch_shark(idx)
    sharks_move()

print(ans)
