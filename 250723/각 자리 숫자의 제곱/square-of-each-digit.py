n = int(input())

# Please write your code here.
def func(x):
    if x < 10:
        return x**2
    m = x % 10
    return func(x // 10) + m**2

print(func(n))