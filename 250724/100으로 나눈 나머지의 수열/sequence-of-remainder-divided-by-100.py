n = int(input())

# Please write your code here.
def func(x):
    if x == 1:
        return 2
    if x == 2:
        return 4
    return func(x-1) * func(x-2) % 100

print(func(n))