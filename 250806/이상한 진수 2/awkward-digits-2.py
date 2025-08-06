a = list(input())

# Please write your code here.
max_num = 0

for i in range(len(a)):
    a[i] = 1 - int(a[i])
    sums = 0
    for j in range(len(a)):
        sums += 2 ** (len(a) - j - 1) * int(a[j])
    max_num = max(max_num, sums)
    a[i] = 1 - int(a[i])

print(max_num)