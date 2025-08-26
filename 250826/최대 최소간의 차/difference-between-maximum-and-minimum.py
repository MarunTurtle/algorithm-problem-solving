import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# arr의 최대 최소를 확인
# 최소 ~ 최소 + k 부터 최대 - k ~ 최대 레인지를 필터링 걸면서 모든 경우의 수의 비용 확인
# 그 중 최소를 저장

max_num = max(arr)
min_num = min(arr)

min_total = sys.maxsize

for i in range(min_num, max_num - k):
    total = 0
    for num in arr:
        if num < i:
            total += abs(i - num)
        elif num > i + k:
            total += abs(num - (i + k))
    
    min_total = min(min_total, total)

print(min_total)