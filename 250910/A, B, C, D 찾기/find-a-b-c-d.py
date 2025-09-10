arr = list(map(int, input().split()))

arr.sort()

a = arr[0]
b = arr[1]

arr.remove(a)
arr.remove(b)
arr.remove(a+b)

c = arr[0]
d = arr[-1] - a - b - c

print(a, b, c, d)