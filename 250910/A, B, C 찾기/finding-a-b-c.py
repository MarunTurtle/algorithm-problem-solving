arr = list(map(int, input().split()))

arr.sort()

a = arr[0]
b = arr[1]
c = arr[-1] - a - b

print(a, b, c)