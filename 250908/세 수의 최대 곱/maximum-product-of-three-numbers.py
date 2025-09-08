from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))

combs = list(combinations(arr, 3))

max_num = float('-inf')

for comb in combs:
    prod = 1
    for num in comb:
        prod *= num

    max_num = max(max_num, prod)

print(max_num)