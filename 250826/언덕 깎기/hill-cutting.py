import sys
input = sys.stdin.readline

n = int(input())
hills = [int(input()) for _ in range(n)]
hills.sort()

lowest = hills[0]
highest = hills[-1]
diff = highest - lowest - 17

min_ans = sys.maxsize

for i in range(diff):
    a = i
    b = diff - i
    min_ans = min(min_ans, a**2 + b**2)



print(min_ans)
