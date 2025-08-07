import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = -sys.maxsize

# Please write your code here.
for i in range(n - k + 1):
    num_sum = 0
    for j in range(i, i+k):
        num_sum += arr[j]
    ans = max(ans, num_sum)

print(ans)