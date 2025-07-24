n = int(input())

# Please write your code here.

def func(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    return func(x//3) + func(x-1)

print(func(n))

