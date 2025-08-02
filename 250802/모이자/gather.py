n = int(input())
A = list(map(int, input().split()))

min_sum = (n * 100) + 1

for i in range(n):
    # print(f"{i}번째")
    cur_sum = 0
    # print(cur_sum)
    for j in range(n):
        distance = abs(i - j)
        cur_sum += A[j] * distance
        # print(f"{cur_sum}, {i} - {j}")
    min_sum = min(min_sum, cur_sum)

print(min_sum)

