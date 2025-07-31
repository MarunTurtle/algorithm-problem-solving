n, m = map(int, input().split())

was_in_diff_place = False

def record_movement(r):
    pos = []
    x = 0
    for i in range(r):
        t, direction = input().split()
        t = int(t)
        for i in range(t):
            if direction == 'L':
                x -= 1
            else:
                x += 1
            pos.append(x)
    return pos

pos_a = record_movement(n)
pos_b = record_movement(m)
max_len = max(len(pos_a), len(pos_b))

if len(pos_a) < max_len:
    pos_a += [pos_a[-1]] * (max_len - len(pos_a))
if len(pos_b) < max_len:
    pos_b += [pos_b[-1]] * (max_len - len(pos_b))

cnt = 0

for i in range(max_len):
    if pos_a[i] == pos_b[i]:
        if was_in_diff_place:
            cnt += 1
        was_in_diff_place = False
    else:
        was_in_diff_place = True

print(cnt)