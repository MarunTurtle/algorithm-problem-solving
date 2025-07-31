n, m = map(int, input().split())
a_loc = []
b_loc = []

a = 0
b = 0

for i in range(n):
    v, t = map(int, input().split())
    for j in range(t):
        a += v
        a_loc.append(a)

for j in range(m):
    v, t = map(int, input().split())
    for k in range(t):
        b += v
        b_loc.append(b)

cnt = 0
leader = 'a'

for i in range(len(b_loc)):
    cur_a = a_loc[i]
    cur_b = b_loc[i]
    prev_leader = leader

    if cur_a > cur_b:
        new_leader = 'a'
    elif cur_a < cur_b:
        new_leader = 'b'
    else:
        new_leader = prev_leader

    if i == 0:
        leader = new_leader
    elif new_leader != prev_leader:
        cnt += 1
        leader = new_leader

print(cnt)