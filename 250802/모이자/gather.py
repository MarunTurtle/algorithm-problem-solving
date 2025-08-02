n = int(input())
A = list(map(int, input().split()))

min_sum = (n * 100) + 1

for i in range(n):
    cur_sum = 0
    for j in range(n):
        distance = abs(i - j)
        cur_sum += A[j] * distance
    min_sum = min(min_sum, cur_sum)

print(min_sum)

