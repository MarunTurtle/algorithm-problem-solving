MAX_K = 100000

n = int(input())

a = [0] * (2 * MAX_K + 1)
cnt_b = [0] * (2 * MAX_K + 1)
cnt_w = [0] * (2 * MAX_K + 1)

b, w, b = 0, 0, 0

cur = MAX_K

for i in range(n):
    x, c = tuple(input().split())