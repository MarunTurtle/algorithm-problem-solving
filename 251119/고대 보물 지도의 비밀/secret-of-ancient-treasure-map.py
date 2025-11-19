import sys
INT_MIN = -sys.maxsize
n, k = map(int, input().split())
nums = [0] + list(map(int, input().split()))

grid = [[INT_MIN] * (k+1) for _ in range(n+1)]

# i번째 라운드에서 음수 카드가 j개 일 때
for i in range(1, n+1):
    for j in range(k+1):
        if nums[i] >= 0:
            if grid[i-1][j] != INT_MIN:
                grid[i][j] = max(nums[i], grid[i-1][j] + nums[i])
            else:
                if j == 0:
                    grid[i][j] = nums[i]
        else:
            if j != 0:
                if grid[i-1][j-1] != INT_MIN:
                    grid[i][j] = max(nums[i], grid[i-1][j-1] + nums[i])
                else:
                    grid[i][j] = nums[i]

print(max(map(max, grid)))

