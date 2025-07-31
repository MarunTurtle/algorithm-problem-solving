n = int(input())

max_len = 0
cnt = 0
prev = 0

for i in range(n):
    x = int(input())

    if i == 0 or prev < x: 
        cnt += 1    
    else:
        cnt = 1
    prev = x
    max_len = max(max_len, cnt)

print(max_len)   