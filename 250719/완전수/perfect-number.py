start, end = map(int, input().split())

cnt = 0
# Please write your code here.
for i in range(start, end + 1):
    
    nums = []
    
    for j in range(1, i):
        if i % j == 0:
            nums.append(j)
    
    if sum(nums) == i:
        cnt += 1

print(cnt)