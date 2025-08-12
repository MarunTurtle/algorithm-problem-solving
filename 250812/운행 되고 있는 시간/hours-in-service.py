n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

max_time = 0

for i in range(n):
    time_frame = [0]*1001
    time = 0
    for j in range(n):
        if j == i:
            continue
        for k in range(a[j], b[j]):
            time_frame[k] = 1

    time = time_frame.count(1)
    max_time = max(time, max_time)

print(max_time)
