start, end = map(int, input().split())

cnt1 = 0

# Please write your code here.
for i in range(start, end+1):
    cnt2 = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt2 += 1
    if cnt2 == 3:
        cnt1 +=1 

print(cnt1)
