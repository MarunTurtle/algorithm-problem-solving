n = int(input())
nums = list(map(int, input().split()))

for i in range(1, nums[0]): # 첫번재 숫자 후보들
    new_nums = [i]
    for j in range(n-1):
        next_num = nums[j] - new_nums[j]
        if next_num <= 0 or next_num in new_nums:
            break
        else:
            new_nums.append(next_num)
    if len(new_nums) == n:
        print(*new_nums)