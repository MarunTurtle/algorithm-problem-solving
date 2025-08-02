n = int(input())
A = list(map(int, input().split()))

min_sum = (n * 100) + 1

for i in range(n):
    # print(f"{i}번째")
    sum = 0
    # print(sum)
    for j in range(n):
        sum += A[j] * abs(i - j)
        # print(f"{sum}, {i} - {j}")
    if sum < min_sum:
        min_sum = sum

print(min_sum)

