import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))
n = 5
ans = sys.maxsize

# uniq_num = set(arr)
# if len(uniq_num) == 1:
#     ans = -1

def diff(i, j, k):
    sum1 = arr[i] + arr[j]
    sum2 = arr[k]
    sum3 = sum(arr) - sum1 - sum2

    max_sum = max(sum1, sum2, sum3)
    min_sum = min(sum1, sum2, sum3)

    return max_sum - min_sum

for i in range(n):
    for j in range(n):
        for k in range(n):
            if k != i or k != j or i != j:
                dif =  diff(i, j, k)
                ans = min(ans, dif)
                # print(f"{i, j, k, l} | {ans}")

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)