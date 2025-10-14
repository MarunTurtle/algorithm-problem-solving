n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

def is_happy(nums):
    max_v = 0
    for i in range(n):
        if i == 0:
            v = 1
        else:
            if nums[i] == nums[i-1]:
                v += 1
            else:
                v = 1
        max_v = max(max_v, v)
    return max_v >= m

for x in range(n):
    nums = [grid[x][i] for i in range(n)]
    if is_happy(nums):
        ans += 1
    
    nums = [grid[i][x] for i in range(n)]
    if is_happy(nums):
        ans += 1
    
print(ans)