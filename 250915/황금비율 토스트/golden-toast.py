n, m = map(int, input().split())
s = list(input())

commands = []
for _ in range(m):
    cmd = input().split()
    if len(cmd) == 1:
        commands.append((cmd[0],))
    else:
        commands.append((cmd[0], cmd[1]))

it = n

for command in commands:
    if command[0] == 'L':
        if it != 0:
            it -= 1
    elif command[0] == 'R':
        if it != n:
            it += 1
    elif command[0] == 'D':
        if it != n:
            s = s[:it] + s[it+1:]
    elif command[0] == 'P':
        s.insert(it, command[1])
        it += 1
        n += 1

        
print(''.join(s))