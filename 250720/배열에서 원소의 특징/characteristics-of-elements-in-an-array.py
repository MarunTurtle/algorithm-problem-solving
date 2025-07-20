nums = list(map(int, input().split()))

for i in range(len(nums)):
    if nums[i] % 3 == 0:
        print(nums[i-1])
        break
