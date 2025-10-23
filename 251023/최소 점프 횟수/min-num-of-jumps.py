n = int(input())
num = list(map(int, input().split()))
ans = n

def dfs(pos, cnt):
    global ans
    if pos == n-1:
        ans = min(ans, cnt)
        return

    if num[pos] == 0:
        return

    for i in range(1, num[pos]+1):
        if pos + i < n:
            dfs(pos + i, cnt+1)
        else:
            continue


dfs(0, 0)

print(ans if ans != n else -1)