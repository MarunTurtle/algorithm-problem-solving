n = int(input())
ans = -1
sec = 0

x, y = 0, 0
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

dict_dir = {
    'E': 0,
    'W': 1,
    'S': 2,
    'N': 3
}

for i in range(n):
    dir_str, t = input().split()
    t = int(t)
    dir_num = dict_dir[dir_str]
    
    for i in range(t):
        x += dx[dir_num]
        y += dy[dir_num]
        sec += 1
        if x == 0 and y == 0:
            ans = sec
            break
    if ans != -1:
        break

print(ans)