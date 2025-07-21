a, b = map(int, input().split())

# Please write your code here.
def is_prime(a, b):
    prime = [True] * (b+1)
    prime[0] = False
    prime[1] = False

    for i in range(2, int(b**0.5) + 1):
        if prime[i]:
            for j in range(i * i, b + 1, i):
                prime[j] = False
    
    ans = []
    for i in range(a, b):
        if prime[i]:
            ans.append(i)
    
    return ans

def sum_digits_is_even(x):
    total = 0
    while x > 0:
        n = x % 10
        total += n
        x = x // 10

    if total % 2 == 0:
        return True
    else:
        return False

primes = is_prime(a, b)

cnt = 0

for num in primes:
    if sum_digits_is_even(num):
        cnt += 1

print(cnt)