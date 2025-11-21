N, M = map(int, input().split())
nums = list(map(int, input().split()))

visited = [0] * N
ans = 0

def dfs(idx, value):
    global ans
    if idx == N:
        if value == M:
            ans += 1 
        return
    
    if value > 20 or value < -20:
        return
    
    if sum(nums[idx:]) == 0:
        ans = 2**len(nums)
        return

    if visited[idx] == 0:
        visited[idx] = 1
        dfs(idx + 1, value + nums[idx])
        dfs(idx + 1, value - nums[idx])
        visited[idx] = 0

dfs(0, 0)
print(ans)