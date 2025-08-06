a = list(map(int, list(input())))
length = len(a)
# Please write your code here.
max_num = 0

for i in range(length):
    a[i] = 1 - a[i]
    
    sums = 0
    for j in range(length):
        sums = sums * 2 + a[j]
    max_num = max(max_num, sums)
    a[i] = 1 - int(a[i])

print(max_num)