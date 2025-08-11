import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

n = 5

ans = sys.maxsize

uniq_num = set(arr)
if uniq_num == 1:
    ans = -1

def diff(i, j, k, l):
    sum1 = arr[i] + arr[j]
    sum2 = arr[k] + arr[l]
    sum3 = sum(arr) - sum1 - sum2

    max_sum = max(sum1, sum2, sum3)
    min_sum = min(sum1, sum2, sum3)

    return max_sum - min_sum

for i in range(n):
    for j in range(i+1, n):
        
        for k in range(n):
            for l in range(k+1, n):
                if k == i or k == j or l == i or l == j:
                    continue
                dif =  diff(i, j, k, l)
                if dif != 0:
                    ans = min(ans, dif)
                    # print(f"{i, j, k, l} | {ans}")

print(ans)