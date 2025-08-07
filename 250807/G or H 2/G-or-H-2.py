n = int(input())
MAX = 100
arr = [0] * (MAX + 1)

for i in range(n):
    idx, letter = input().split()
    idx = int(idx)
    arr[idx] = 1 if letter == 'G' else 2

max_size = 0

#H, G 각각 최댓값
for i in range(MAX + 1):
    size = 0
    if arr[i] == 0:
        continue
    for j in range(i, MAX + 1):
        if arr[j] == arr[i]:
            size = j - i
        else:
            break
        max_size = max(size, max_size)

# GH 정확히 같은 갯수
for i in range(MAX + 1):
    size = 0
    if arr[i] == 0:
        continue
    for j in range(i, MAX + 1):
        if arr[j] == 0:
            continue
        temp_arr = arr[i:j+1]
        if temp_arr.count(1) == temp_arr.count(2):
            size = j - i
            max_size = max(size, max_size)

print(max_size)