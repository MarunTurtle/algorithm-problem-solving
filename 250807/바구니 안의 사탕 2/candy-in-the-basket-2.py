MAX_NUM = 100

n, k = map(int, input().split())
arr = [0] * (MAX_NUM + 1)

for _ in range(n):
    q, idx = map(int, input().split())
    arr[idx] += q

max_sum = 0

for i in range(MAX_NUM + 1):
    left = max(0, i - k)
    right = min(MAX_NUM, i + k)
    cur_sum = sum(arr[left:right+1])
    max_sum = max(max_sum, cur_sum)

print(max_sum)