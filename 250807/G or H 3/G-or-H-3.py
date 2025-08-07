import sys

n, k = map(int, input().split())
arr = [0] * 10002
max_sum = -sys.maxsize

for _ in range(n):
    idx, alphabet = input().split()
    idx = int(idx)
    arr[idx] = 1 if alphabet == 'G' else 2

for i in range(1, 10001 - k + 1):  # 슬라이딩 시작점
    num_sum = 0
    for j in range(i, i + k + 1):      # 길이 k 구간 합
        num_sum += arr[j]
    max_sum = max(num_sum, max_sum)

print(max_sum)