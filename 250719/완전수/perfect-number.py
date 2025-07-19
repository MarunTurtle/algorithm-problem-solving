start, end = map(int, input().split())

cnt = 0
# Please write your code here.
for i in range(start, end + 1):
    
    divisble_sum = 0
    
    for j in range(1, i):
        if i % j == 0:
            divisble_sum += j
        
    if divisble_sum == i:
        cnt += 1

print(cnt)