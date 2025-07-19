n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
max_num = -1

for i in range(1, n):
    if nums.count(nums[i]) > 1:
        continue
    if nums[i] > max_num:
        max_num = nums[i]

print(max_num)