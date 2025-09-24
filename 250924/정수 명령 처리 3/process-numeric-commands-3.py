from collections import deque

n = int(input())
q = deque()

for i in range(n):
    command = input().split()
    if command[0] == 'push_back':
        q.append(int(command[1]))
    elif command[0] == 'push_front':
        q.appendleft(int(command[1]))    
    elif command[0] == 'pop_front':
        print(q[0])
        q.popleft()
    elif command[0] == 'pop_back':
        print(q[-1])
        q.pop()
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        print(1) if len(q) == 0 else print(0)
    elif command[0] == 'front':
        print(q[0])
    elif command[0] == 'back':
        print(q[-1])

