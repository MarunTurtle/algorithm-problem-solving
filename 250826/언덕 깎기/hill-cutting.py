n = int(input())
hills = [int(input()) for _ in range(n)]
hills.sort()

lowest = hills[0]
highest = hills[-1]
diff = highest - lowest - 17

a = diff // 2
b = diff - a

# print(a, b)
print(a**2 + b**2)

