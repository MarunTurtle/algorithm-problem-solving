n = int(input())
arr = list(map(int, input().split()))

def lower_bound(dp, target):
    l, r = 0, len(dp)
    mid = (l + r) // 2
    while l < r:
        if dp[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l

dp = []

for i in range(n):
    idx = lower_bound(dp, arr[i])

    if idx == len(dp):
        dp.append(arr[i])
    else:
        dp[idx] = arr[i]

print(len(dp))
    
