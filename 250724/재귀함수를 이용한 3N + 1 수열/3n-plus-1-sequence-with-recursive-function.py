n = int(input())

# Please write your code here.
def func(x):
    if x == 1:
        return 0
    if x % 2 == 0:
        y = x // 2
    else:
        y = (x * 3) + 1
    return 1 + func(y)

print(func(n))