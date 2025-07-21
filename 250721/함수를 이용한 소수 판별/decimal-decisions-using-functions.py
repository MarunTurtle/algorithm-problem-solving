a, b = map(int, input().split())

# Please write your code here.
def is_prime(a, b):
    prime = [True] * (b + 1)
    prime[0] = False
    prime[1] = False

    for i in range(int(b**0.5 + 1)):
        if prime[i] == True:
            for j in range(i+1, b+1):
                if j % i == 0:
                    prime[j] = False

    total = 0
    for i in range(a, b+1):
        if prime[i] == True:
            total += i
    return total

print(is_prime(a, b))