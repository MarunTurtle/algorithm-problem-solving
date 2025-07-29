n = int(input())
x = 0
history = {}

for i in range(n):
    m, direction = input().split()
    m = int(m)
    for j in range(m):
        if direction == 'L':
            x -= 1
            if x in history.keys():
                history[x] += 1
            else: 
                history[x] = 1
        else:
            x += 1
            if x in history.keys():
                history[x] += 1
            else: 
                history[x] = 1

cnt = 0

for i in history.values():
    if i >= 2:
        cnt +=1 

print(cnt)