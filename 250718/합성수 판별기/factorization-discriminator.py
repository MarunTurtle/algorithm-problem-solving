n = int(input())

satisfied  = False

for i in range(2, n):
    if n % i == 0:
        satisfied = True

print('C') if satisfied else print('N')