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
    for i in range(a, b+1):
        if prime[i]:
            ans.append(i)
    
    return ans

def sum_digits_is_even(x):
    return sum(int(d) for d in str(x)) % 2 == 0

primes = is_prime(a, b)

cnt = 0

for num in primes:
    if sum_digits_is_even(num):
        cnt += 1

print(cnt)