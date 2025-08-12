import sys
input = sys.stdin.readline

n, budget = map(int, input().split())
presents = [int(input()) for _ in range(n)]
max_count = 0

for i in range(n):
    prices = presents[:]  
    prices[i] //= 2  # i번째 상품 할인 적용
    prices.sort()    # 싼 것부터 구매

    count = 0
    budget_cut = budget
    for price in prices:
        if budget_cut >= price:
            budget_cut -= price
            count += 1
        else:
            break

    max_count = max(max_count, count)

print(max_count)
