from collections import deque

n, k = map(int, input().split())

# Please write your code here.
q = deque()
ans = []
for i in range(1, n+1):
    q.append(i)

while len(q) != 1:
    for i in range(k-1):
        q.append(q[0])
        q.popleft()
    ans.append(q[0])
    q.popleft()
    
if len(q) != 0:
    for a in q:
        ans.append(a)

print(*ans)