import sys
MAX_VALUE = sys.maxsize

ans = -MAX_VALUE

n = int(input())
nums = list(map(int, input().split()))

for i in range(n-2):
    for j in range(i+2, n):
        sum_num = nums[i] + nums[j]
        ans = max(ans, sum_num)

print(ans)
