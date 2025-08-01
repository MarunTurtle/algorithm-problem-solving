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

def move(dir_num, t):
    global x, y
    global ans, sec

    for _ in range(t):
        x += dx[dir_num]
        y += dy[dir_num]
        sec += 1
        if x == 0 and y == 0:
            ans = sec
            return True
    return False

for i in range(n):
    dir_str, t = input().split()
    t = int(t)
    dir_num = dict_dir[dir_str]
    
    if move(dir_num, t):
        break
    
print(ans)