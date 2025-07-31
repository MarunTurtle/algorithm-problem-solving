n, t = map(int, input().split())
nums = list(map(int, input().split()))

max_len = 0
cnt = 0

for i in range(n):
    if nums[i] > t:
        cnt += 1
    else:
        cnt = 0
    max_len = max(cnt, max_len)

print(max_len)