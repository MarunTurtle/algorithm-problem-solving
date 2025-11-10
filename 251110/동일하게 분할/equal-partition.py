import sys
n = int(input())
arr = [0] + list(map(int, input().split()))
m = sum(arr)

if m % 2 == 1:
    print('No')
    sys.exit()

reachable = [False] * (m + 1)
reachable[0] = True

for j in range(1, n):
    for i in range(m, j-1, -1):
        if reachable[i - arr[j]]:
            reachable[i] = True

if reachable[m//2]:
    print('Yes')
else:
    print('No')