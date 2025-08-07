n = int(input())
arr = [0] * 101

for i in range(n):
    idx, letter = input().split()
    idx = int(idx)
    arr[idx] = 1 if letter == 'G' else 2

max_size = 0

#G 최댓값
for i in range(n):
    size = 0
    if i != 1:
        continue
    for j in range(i, n):
            




for i in range(n):
    if arr[i] == 0:
            continue
    for j in range(i, n):
        if arr[j] == 0:
            continue
        