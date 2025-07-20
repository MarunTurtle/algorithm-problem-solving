from collections import deque

n = int(input())
d = deque()

nums = list(map(int, input().split()))

for num in nums:
    if num % 2 == 0:
        d.append(num)

for i in range(len(d)):
    print(d.pop(), end=" ")