n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
idx = a.index(max(a))
print(idx+1, end=" ")
print(a[0:idx].index(max(a[0:idx]))+1)