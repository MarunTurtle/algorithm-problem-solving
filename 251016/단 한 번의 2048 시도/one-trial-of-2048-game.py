n = 4
grid = [list(map(int, input().split())) for _ in range(n)]
dir = input()

def move_right():
    for r in range(n):
        tmp = [0] * n
        cur_idx = n-1
        for i in range(n-1, -1, -1):
            num = grid[r][i]
            if num != 0:
                tmp[cur_idx] = num
                cur_idx -= 1
        
        res_temp = [0] * n
        cur_idx = n-1
        skip = []
        for i in range(n-1, -1, -1):
            if i in skip:
                continue
            if i == 0:
                res_temp[cur_idx] = tmp[i]
            elif tmp[i] == tmp[i-1]:
                res_temp[cur_idx] = tmp[i] * 2
                cur_idx -= 1
                skip.append(i-1)
            else:
                res_temp[cur_idx] = tmp[i]
                cur_idx -= 1

        grid[r] = res_temp

def move_left():
    for r in range(n):
        tmp = [0] * n
        cur_idx = 0
        for i in range(n):
            num = grid[r][i]
            if num != 0:
                tmp[cur_idx] = num
                cur_idx += 1

        res_temp = [0] * n
        cur_idx = 0
        skip = []
        for i in range(n):
            if i in skip:
                continue
            if i == n-1:
                res_temp[cur_idx] = tmp[i]
            elif tmp[i] == tmp[i+1]:
                res_temp[cur_idx] = tmp[i] * 2
                cur_idx += 1
                skip.append(i+1)
            else:
                res_temp[cur_idx] = tmp[i]
                cur_idx += 1

        grid[r] = res_temp

def move_down():
    for c in range(n):
        tmp = [0] * n
        cur_idx = n-1
        for i in range(n-1, -1, -1):
            num = grid[i][c]
            if num != 0:
                tmp[cur_idx] = num
                cur_idx -= 1

        res_temp = [0] * n
        cur_idx = n-1
        skip = []
        for i in range(n-1, -1, -1):
            if i in skip:
                continue
            if i == 0:
                res_temp[cur_idx] = tmp[i]
            elif tmp[i] == tmp[i-1]:
                res_temp[cur_idx] = tmp[i] * 2
                cur_idx -= 1
                skip.append(i-1)
            else:
                res_temp[cur_idx] = tmp[i]
                cur_idx -= 1
        
        for i in range(n):
            grid[i][c] = res_temp[i] 

def move_up():
    for c in range(n):
        tmp = [0] * n
        cur_idx = 0
        for i in range(n):
            num = grid[i][c]
            if num != 0:
                tmp[cur_idx] = num
                cur_idx += 1
        
        res_temp = [0] * n
        cur_idx = 0
        skip = []
        for i in range(n):
            if i in skip:
                continue
            if i == n-1:
                res_temp[cur_idx] = tmp[i]
            elif tmp[i] == tmp[i+1]:
                res_temp[cur_idx] = tmp[i]* 2
                cur_idx += 1
                skip.append(i+1)
            else:
                res_temp[cur_idx] = tmp[i]
                cur_idx += 1
        
        for i in range(n):
            grid[i][c] = res_temp[i] 

if dir == 'R':
    move_right()
elif dir == 'L':
    move_left()
elif dir == 'U':
    move_up()
else:
    move_down()

for row in grid:
    print(*row)
        