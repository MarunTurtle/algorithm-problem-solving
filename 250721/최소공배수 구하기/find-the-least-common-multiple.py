n, m = map(int, input().split())

# Please write your code here.
def lcm(n, m):
    gcd = 0
    for i in range(min(n, m)):
        if n % (i+1) == 0 and m % (i+1) == 0 and (i+1) > gcd:
            gcd = i+1
    
    print(gcd * (n // gcd) * (m // gcd))

lcm(n, m)