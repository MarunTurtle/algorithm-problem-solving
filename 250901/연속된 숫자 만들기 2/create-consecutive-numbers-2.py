n = 3
pos = list(map(int, input().split()))

diff12 = pos[1] - pos[0]
diff23 = pos[2] - pos[1]

if diff12 == 1 and diff23 == 1:
    print(0)
elif diff12 == 2 or diff23 == 2:
    print(1)
elif diff12 == 1 or diff23 == 1:
    print(1)
else:
    print(2)

