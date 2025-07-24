# 입력
n = int(input())
arr = list(map(int, input().split()))

def lcm(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    
    return a * b // gcd

def get_lcm_all(index):
    if index == 1:
        return arr[1]
    return lcm(get_lcm_all(index - 1), arr[index])

print(get_lcm_all(n))