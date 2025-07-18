n = int(input())

exp = 1

while n != 1:
    if n % 2 == 0:
        exp += 1
    n /= 2

print(exp)