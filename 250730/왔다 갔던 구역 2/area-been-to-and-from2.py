n = int(input())
x = 0
history = {}

for i in range(n):
    m, direction = input().split()
    m = int(m)
    for j in range(m):
        if direction == 'L':
            x -= 1
        else:
            x += 1
        
        if x in history:
            history[x] += 1
        else: 
            history[x] = 1

cnt = sum(1 for count in history.values() if count >= 2)

print(cnt)