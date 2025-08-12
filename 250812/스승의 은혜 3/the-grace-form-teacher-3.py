n, budget = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(n)]
gifts.sort(key= lambda x: (x[0] + x[1], x[0]))
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

# Please write your code here.
# print(gifts)


ans = 0

for i in range(n):
    cur_budget = budget
    count = 0
    for j in range(n):
        if j == i:
            present_price = (P[j] // 2) + S[j]
            # print(f"{j} 번째 선물: {P[j]} 배송: {S[j]}")
        else:
            present_price = P[j] + S[j]
        
        if cur_budget < present_price:
            continue
        else:
            # print(f"{j} 번째 현재 선물 가격:{present_price}")
            cur_budget -= present_price
            count += 1
    # print(f"{i}번이 할인")
    # print(count)
    ans = max(ans, count)

print(ans)