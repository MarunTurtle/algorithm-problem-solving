n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
for _ in range(t):
    tmp = l[n-1]
    
    for i in range(n-1, 0, -1):
        l[i] = l[i-1]
    l[0] = d[n-1]
    
    tmp2 = r[n-1]
    for i in range(n-1, 0, -1):
        r[i] = r[i-1]
    r[0] = tmp

    for i in range(n-1, 0, -1):
        d[i] = d[i-1]
    d[0] = tmp2

print(*l)
print(*r)
print(*d)