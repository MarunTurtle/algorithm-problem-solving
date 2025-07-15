n = int(input())

sizes = list(map(int, input().split()))

t, p = map(int, input().split())

def count_t(t, sizes):
    cnt = 0
    
    for size in sizes:
        if size == 0:
          continue
        if size % t == 0:
          cnt += size // t
        else:
          cnt += size // t + 1
    return cnt

def count_p(p, n):
    bundle = n // p
    rmnder = n - (bundle * p)
    return bundle, rmnder

a1 = count_t(t, sizes)
a2 = count_p(p, n)

print(a1)
for num in a2:
    print(num, end=" ")