n = int(input())
blocks = [int(input()) for _ in range(n)]
blocks.sort(reverse=True)
ans = float('inf')

min_num = blocks[n-1]
max_num = blocks[0]

for mean in range(min_num, max_num+1):
    total = 0
    for number in blocks:
        total += abs(mean - number)

    ans = min(ans, total//2)

print(ans)