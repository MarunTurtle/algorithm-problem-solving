import sys
MAX_NUM = 10000
n, k = map(int, input().split())
arr = [0] * (MAX_NUM + 1)
max_sum = -sys.maxsize

for _ in range(n):
    idx, alphabet = input().split()
    idx = int(idx)
    arr[idx] = 1 if alphabet == 'G' else 2

cur_slide = sum(arr[:k+1])
max_sum = cur_slide

for i in range(1, MAX_NUM - k + 1):  # 슬라이딩 시작점
    cur_slide = cur_slide - arr[i-1] + arr[i+k]
    max_sum = max(cur_slide, max_sum)

print(max_sum)