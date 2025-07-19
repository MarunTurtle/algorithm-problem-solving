n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
max_profit = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        curr_profit = price[j] - price[i]
        if curr_profit > max_profit:
            max_profit = curr_profit

print(max_profit)
