import math

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# def lcm(a, b):
#     return (a * b) // gcd(a, b)

def solution(numer1, denom1, numer2, denom2):
    
    # 1. 공통 분모 구하기
    # common_denom = lcm(denom1, denom2)
    lcm = (denom1 * denom2) // math.gcd(denom1, denom2)
    
    # 2. 통분한 분자 계산
    # new_numer = numer1 * (common_denom // denom1) + numer2 * (common_denom // denom2)
    numer = numer1 * (lcm // denom1) + numer2 * (lcm // denom2)
    
    # 3. 기약분수로 만들기
    # common_gcd = gcd(new_numer, common_denom)
    gcd = math.gcd(numer, lcm)
    
    a = 2
    
    return [numer // gcd, lcm // gcd]
