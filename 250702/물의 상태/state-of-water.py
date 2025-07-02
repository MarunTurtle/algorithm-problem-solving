n = int(input())


if n < 0:
    ans = 'ice'
elif n >= 100:
    ans = 'vapor'
else:
    ans = 'water'

print(ans)