a, b = map(int, input().split())

# Please write your code here.
def is_prime(a, b):
    prime = [True] * (b + 1)
    prime[0] = False
    prime[1] = False

    for i in range(2, int(b**0.5) + 1):
        if prime[i]:
            for j in range(i * i, b + 1, i):
                if j % i == 0:
                    prime[j] = False

    total = 0
    for i in range(a, b+1):
        if prime[i] == True:
            total += i
    return total

print(is_prime(a, b))