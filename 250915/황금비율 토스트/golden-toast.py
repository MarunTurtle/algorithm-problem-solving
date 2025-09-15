n,m = map(int, input().split())
str = input()
idx = n+1
maxidx = n+1

for i in range(m):
    com = input()
    if com[0] == 'P':
        a,b = com.split()
        str = str[:idx-1:] + b + str[idx-1::]
        maxidx += 1
        idx += 1
    else:
        if com == 'L':
            if idx != 0:
                idx -= 1
        elif com == 'R':
            if idx != maxidx:
                idx += 1
        else:
            if idx == maxidx:
                continue
            else:
                str = str[:idx - 1] + str[idx:]
                maxidx -= 1
print(str)
