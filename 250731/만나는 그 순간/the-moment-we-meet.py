MAX_T = 1000

a_loc = []
b_loc = []

a = 0
b = 0

n, m = map(int, input().split())

for i in range(n):
    direction, t = input().split()
    t = int(t)

    for i in range(t):    
        if direction == 'L':
            a -= 1
        else:
            a += 1
        a_loc.append(a)

for i in range(m):
    direction, t = input().split()
    t = int(t)

    for i in range(t):    
        if direction == 'L':
            b -= 1
        else:
            b += 1
        b_loc.append(b)

sec = 1

def get_time():
    global sec
    for i in range(len(a_loc)):
        if a_loc[i] == b_loc[i]:
            return sec
        else:
            sec += 1
    return -1

print(get_time())