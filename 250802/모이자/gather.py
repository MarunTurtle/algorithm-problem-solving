n = int(input())
A = list(map(int, input().split()))

min_sum = float('inf')

for i in range(n):  # i: 사람들이 모일 집의 인덱스
    cur_sum = 0
    for j in range(n):
        distance = abs(i - j)
        cur_sum += A[j] * distance  # j번 집에 있는 A[j]명 모두 이동
    min_sum = min(min_sum, cur_sum)

print(min_sum)