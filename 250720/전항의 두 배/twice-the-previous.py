nums = list(map(int, input().split()))

for i in range(8):
    nums.append((nums[i]*2) + nums[i+1])

print(*nums)