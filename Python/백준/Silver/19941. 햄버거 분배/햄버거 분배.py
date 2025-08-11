import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().strip())
ans = 0

for i, ch in enumerate(arr):
    if ch != 'P':
        continue
    left = max(0, i - K)
    right = min(N - 1, i + K)
    for j in range(left, right + 1):
        if arr[j] == 'H':
            ans += 1
            arr[j] = 'X' 
            break

print(ans)
