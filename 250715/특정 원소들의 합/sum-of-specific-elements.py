total = 0

for i in range(1, 5):
    nums = list(map(int, input().split()))
    for j in range(0, i):
        total += nums[j]

print(total)