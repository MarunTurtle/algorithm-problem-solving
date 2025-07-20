n = int(input())
nums = list(map(int, input().split()))

min_n = float('inf')

for i in range(n-1):
    for j in range(i + 1, n):
        temp = abs(nums[i] - nums[j])
        if temp < min_n:
            min_n = temp

print(min_n)