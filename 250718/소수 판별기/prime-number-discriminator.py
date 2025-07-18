n = int(input())

is_prime = False

for i in range(2, n):
    if n % i == 0:
        is_prime = True

print('P') if is_prime else print('C')