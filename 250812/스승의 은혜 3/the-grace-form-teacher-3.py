n, budget = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(n)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

# Please write your code here.
gifts.sort(key= lambda x: x[0])

ans = 0

for i in range(n):
    cur_budget = budget
    count = 0
    for j in range(n):
        if j == i:
            present_price = (P[j] // 2) + S[j]
        else:
            present_price = P[j] + S[j]
        
        if cur_budget < present_price:
            continue
        else:
            cur_budget -= present_price
            count += 1
    ans = max(ans, count)

print(ans)