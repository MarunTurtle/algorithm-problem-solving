MAX_NUM = 100

n, k = map(int, input().split())
arr = [0] * (MAX_NUM + 1)

for _ in range(n):
    q, idx = map(int, input().split())
    arr[idx] += q

max_sum = 0

for i in range(MAX_NUM - k + 2):
    if i - k > 0 and i + k <= MAX_NUM:
        cur_sum = sum(arr[i-k:i+k+1])
    elif i - k <= 0 and i + k > MAX_NUM:
        cur_sum = sum(arr)
    elif i - k <= 0:
        cur_sum = sum(arr[0:i+k+1])
    else:
        cur_sum = sum(arr[i-k:])
    max_sum = max(max_sum, cur_sum)

print(max_sum)

