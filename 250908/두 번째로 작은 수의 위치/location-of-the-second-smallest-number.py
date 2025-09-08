n = int(input())
numbers = list(map(int, input().split()))
nums = sorted(numbers)

min_num = nums[0]
min_count = 1
second_min_num = -1

for i in range(1, n):
    if nums[i] == min_num:
        min_count += 1
    if nums[i] == second_min_num:
        second_min_num = -1
        break    
    if nums[i] > second_min_num and second_min_num != -1:
        break
    if nums[i] > min_num:
        second_min_num = nums[i]

if second_min_num == -1:
    print(-1)
else:
    print(numbers.index(second_min_num) + 1)