n = int(input())
arr = list(map(int, input().split()))
m = sum(arr)

reachable = [False] * (m + 1)
reachable[0] = True

for a in arr:
    for s in range(m, a - 1, -1):
        if reachable[s - a]:
            reachable[s] = True

ans = min(abs(m - 2*s) for s in range(1, m) if reachable[s])
print(ans)
