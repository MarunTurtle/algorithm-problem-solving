def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


n = int(input())
nums = list(map(int, input().split()))

dp = []

for num in nums:
    idx = lower_bound(dp, num)
    # 삽입 위치가 dp 끝이라면 append
    if idx == len(dp):
        dp.append(num)
    else:
        dp[idx] = num

print(len(dp))
