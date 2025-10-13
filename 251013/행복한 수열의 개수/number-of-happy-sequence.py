n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

def is_happy(nums):
    max_count = 0
    cur_count = 1
    cur_num = nums[0]
    for i in range(1, n):
        if nums[i] == cur_num:
            cur_count += 1
        else:
            cur_count = 1
            cur_num = nums[i]
        max_count = max(max_count, cur_count)
    if max_count >= m:
        return True
    return False

for x in range(n):
    nums = [grid[x][i] for i in range(n)]
    if is_happy(nums):
        ans += 1

    nums = [grid[i][x] for i in range(n)]
    if is_happy(nums):
        ans += 1

print(ans)