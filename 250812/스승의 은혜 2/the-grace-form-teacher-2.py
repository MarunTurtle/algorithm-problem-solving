import sys
input = sys.stdin.readline

# 1 <= n <= 1 000
# 1 <= b <= 1 000
# 0 <= price <= 1 000 (ALWAYS EVEN)

n, budget = map(int, input().split())
presents = [int(input()) for _ in range(n)]
max_count = 0

for i in range(n):
    count = 0
    budget_cut = budget
    for j in range(n):
        present_price = 0
        if j == i:
            present_price = (presents[j]//2)
        else:
            present_price = presents[j]
        
        if budget_cut < present_price:
            continue
        else:
            budget_cut -= present_price
            count += 1
    max_count = max(count, max_count)

print(max_count)
