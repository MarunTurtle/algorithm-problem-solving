am, ae = map(int, input().split())
bm, be = map(int, input().split())


if am > bm:
    print('A')
elif am == bm:
    if ae > be:
        print('A')
    else:
        print('B')
else:
    print('B')