n = int(input())

for i in range(1, n+1):
    print(' / '.join(f"{i} * {j} = {i*j}" for j in range(1, n - i + 2)))
    
    