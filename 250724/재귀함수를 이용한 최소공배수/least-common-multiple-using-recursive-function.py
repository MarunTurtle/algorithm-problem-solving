n = int(input())
arr = [0] + list(map(int, input().split()))

def gcd(x, y):
    gcd = 1
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            gcd = i
    return gcd

def lcm(x, y):
    return x * y // gcd(x, y)

def lcm_list(idx):
    if idx == 1:
        return arr[idx]
    return lcm(arr[idx], lcm_list(idx - 1))

print(lcm_list(n))
