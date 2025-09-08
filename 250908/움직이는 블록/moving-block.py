n = int(input())
blocks = [int(input()) for _ in range(n)]
blocks.sort(reverse=True)
ans = float('inf')

min_num = blocks[n-1]
max_num = blocks[0]

total_sum = 0
for i in range(n):
    total_sum += blocks[i]

mean = total_sum // n

total = 0
for number in blocks:
    total += abs(mean - number)

ans = min(ans, total//2)

print(ans)