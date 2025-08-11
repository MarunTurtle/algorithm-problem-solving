import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))
n = 5
ans = sys.maxsize

# uniq_num = set(arr)
# if len(uniq_num) == 1:
#     ans = -1

def diff(i, j, k):    
    sum1 = arr[i]
    sum2 = arr[k] + arr[j]
    sum3 = sum(arr) - sum1 - sum2

    if sum1 == sum2 or sum2 == sum3 or sum3 == sum1:
        return sys.maxsize

    max_sum = max(sum1, sum2, sum3)
    min_sum = min(sum1, sum2, sum3)

    return max_sum - min_sum

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j or j != k or i != k:
                dif =  diff(i, j, k)
                ans = min(ans, dif)
                # print(f"{i, j, k, l} | {ans}")

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)