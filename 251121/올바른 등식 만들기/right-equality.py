N, M = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0

def dfs(idx, value):
    global ans
    
    if value > 20 or value < -20:
        return
    
    if idx == N:
        if value == M:
            ans += 1 
        return
    
    if sum(nums[idx:]) == 0:
        ans = 2**len(nums)
        return

    dfs(idx + 1, value + nums[idx])
    dfs(idx + 1, value - nums[idx])


dfs(0, 0)
print(ans)