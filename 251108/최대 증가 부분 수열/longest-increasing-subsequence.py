n = int(input())
arr = list(map(int, input().split()))

def lower_bound(dp, target):
    l, r = 0, len(dp)
    while l < r:
        mid = (l + r) // 2
        if dp[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l

dp = []

for i in range(n):
    idx = lower_bound(dp, arr[i])

    if idx == len(dp):
        dp.append(arr[i])
    else:
        dp[idx] = arr[i]

print(len(dp))
    
