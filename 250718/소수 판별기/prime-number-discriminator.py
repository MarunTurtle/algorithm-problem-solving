n = int(input())

is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False

print('P') if is_prime else print('C')