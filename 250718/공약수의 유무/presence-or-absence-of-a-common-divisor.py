a, b = map(int, input().split())

exist = False

for i in range(a, b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        exist = True

print(1) if exist else print(0)