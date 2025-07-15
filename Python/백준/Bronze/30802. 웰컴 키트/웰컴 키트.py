n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())

def count_t(t, sizes):
    return sum((s + t - 1) // t for s in sizes)

def count_p(p, n):
    bundle = n // p
    rmnder = n % p
    return bundle, rmnder

a1 = count_t(t, sizes)
a2 = count_p(p, n)

print(a1)
for num in a2:
    print(num, end=" ")