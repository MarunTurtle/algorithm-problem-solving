from collections import deque
n = int(input())
q = deque()

for i in range(n):
    command = input().split()
    if command[0] == 'push':
        q.append(int(command[1]))
    elif command[0] == 'pop':
        print(q[0])
        q.popleft()
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        print(1) if len(q) == 0 else print(0)
    elif command[0] == 'front':
        print(q[0])

