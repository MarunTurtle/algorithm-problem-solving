import math

# 최대공약수 (GCD)
def gcd(a, b):
    return math.gcd(a, b)

# 최소공배수 (LCM) - 두 수
def lcm(a, b):
    return a * b // gcd(a, b)

# 리스트의 LCM (재귀)
def lcm_list(arr, idx=0):
    if idx == len(arr) - 1:
        return arr[idx]
    return lcm(arr[idx], lcm_list(arr, idx + 1))

# 입력
n = int(input())
arr = list(map(int, input().split()))

# 출력
print(lcm_list(arr))