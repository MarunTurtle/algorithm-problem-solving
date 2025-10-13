n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

def is_happy(nums):
    max_count = 1
    cur_count = 1
    for i in range(1, n):
        if nums[i-1] == nums[i]:
            cur_count += 1
        else:
            cur_count = 1
        max_count = max(max_count, cur_count)
    
    return max_count >= m

for x in range(n):
    nums = [grid[x][i] for i in range(n)]
    if is_happy(nums):
        ans += 1

    nums = [grid[i][x] for i in range(n)]
    if is_happy(nums):
        ans += 1

print(ans)