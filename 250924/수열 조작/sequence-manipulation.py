from collections import deque

n = int(input())
dq = deque()

# Please write your code here.
for i in range(1, n+1):
    dq.append(i)

while len(dq) > 1:
    # print(*dq)
    dq.popleft()
    dq.append(dq[0])
    dq.popleft()

print(dq[0])