n, m = map(int, input().split())

winner = 0
pos_a = []
pos_b = []
a = 0
b = 0

for i in range(n):
    v, t = map(int, input().split())
    for j in range(t):
        a += v
        pos_a.append(a)

for i in range(m):
    v, t = map(int, input().split())
    for j in range(t):
        b += v
        pos_b.append(b)

cnt = 0

for t in range(len(pos_a)):
    if pos_a[t] == pos_b[t]:
        new_winner = 3
    else:
        if pos_a[t] > pos_b[t]:
            new_winner = 1
        else:
            new_winner = 2 
    if new_winner != winner:
        cnt += 1
        winner = new_winner

print(cnt)