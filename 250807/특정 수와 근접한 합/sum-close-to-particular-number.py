import sys

n, s = map(int, input().split())
nums = list(map(int, input().split()))

min_diff = sys.maxsize 

for i in range(n-1):
    for j in range(i+1, n):
        num_sum = sum(nums) - nums[i] - nums[j]
        diff = abs(s - num_sum)
        min_diff = min(min_diff, diff)

print(min_diff)