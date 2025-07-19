n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
print(max(a), end=" ")

m = max(a)
a.remove(m)

print(max(a))

