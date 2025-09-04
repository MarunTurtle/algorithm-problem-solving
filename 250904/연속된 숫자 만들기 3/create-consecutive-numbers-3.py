nums = list(map(int, input().split()))
ans = 0

diff1 = nums[1] - nums[0]
diff2 = nums[2] - nums[1]

x = max(diff1, diff2)
print(x - 1)