n, r, c = map(int, input().split())

a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

num_list = [a[r][c]]

while True:
    moved = False
    cur_num = a[r][c]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 1 <= nr <= n and 1 <= nc <= n:        
            if a[nr][nc] > cur_num:
                r, c = nr, nc
                num_list.append(a[nr][nc])
                moved = True
                break

    if not moved:
        break
        
print(*num_list)    

    