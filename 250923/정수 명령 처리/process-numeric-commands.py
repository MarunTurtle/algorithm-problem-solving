N = int(input())
command = []
stack = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        stack.append(int(line[1]))
    elif line[0] == "size":
        print(len(stack))
    elif line[0] == "pop":
        print(stack.pop())
    elif line[0] == 'empty':
        print('1') if len(stack) == 0 else print('0')
    elif line[0] == 'top':
        print(stack[-1])
