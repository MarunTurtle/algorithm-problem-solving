nums = list(map(int, input().split()))

max_under = float('-inf')
min_over = float('inf')

for num in nums:
    if num < 500 and num > max_under:
        max_under = num
    elif num >= 500 and num < min_over:
        min_over = num

print(max_under, min_over)