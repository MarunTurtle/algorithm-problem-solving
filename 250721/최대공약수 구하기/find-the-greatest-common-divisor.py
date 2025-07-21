n, m = map(int, input().split())

# Please write your code here.
def gcd(n, m):
    ans = 0
    for i in range(min(n, m)):
        if n % (i+1) == 0 and m % (i+1) == 0 and (i+1) > ans:
            ans = i+1
    print(ans)

gcd(n, m)