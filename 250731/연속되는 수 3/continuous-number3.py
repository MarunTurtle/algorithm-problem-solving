n = int(input())
max_len = 0
prev = True
cnt = 0

def define(x):
    return True if x > 0 else False

for i in range(n):
    x = int(input())
    if i == 0 or (prev != define(x)):
        max_len = max(max_len, cnt)
        cnt = 1
        prev = define(x)
    else:
        cnt += 1

max_len = max(max_len, cnt)

print(max_len)