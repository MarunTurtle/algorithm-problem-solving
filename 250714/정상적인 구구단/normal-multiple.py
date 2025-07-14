n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if j == n:
            print(f"{i} * {j} = {i*j}")
        else:
            print(f"{i} * {j} = {i*j}", end=', ')