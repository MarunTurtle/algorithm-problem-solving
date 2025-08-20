import sys

n = int(input())
nums = list(map(int, input().split()))
min_sum = sys.maxsize

for i in range(n):
    for j in range(n):
        new_num = nums[:]
        new_num[i] *= 2
        del new_num[j] 

        sum_diff = 0
        for k in range(len(new_num)-1):
            sum_diff += abs(new_num[k] - new_num[k+1])
        min_sum = min(sum_diff, min_sum)

print(min_sum)
            