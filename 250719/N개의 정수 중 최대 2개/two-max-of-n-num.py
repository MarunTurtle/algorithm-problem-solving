n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
if a[0] > a[1]:
    max1, max2 = a[0], a[1]
else:
    max1, max2 = a[1], a[0]

for i in range(2, n):
    if a[i] >= max1:
        max2 = max1
        max1 = a[i]
    elif a[i] > max2:
        max2 = a[i]

print(max1, max2)