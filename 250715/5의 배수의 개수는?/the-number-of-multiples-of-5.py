cnt = 0

for _ in range(4):
    nums = list(map(int, input().split()))
    for num in nums:
        if num % 5 == 0:
            cnt += 1

print(cnt)
