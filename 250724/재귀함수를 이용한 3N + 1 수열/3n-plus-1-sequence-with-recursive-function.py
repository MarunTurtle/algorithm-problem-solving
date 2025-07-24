n = int(input())

# Please write your code here.
def func(x):
    if x == 1:
        return 0
    if x % 2 == 0:
        return 1 + func(x//2)
    else:
        return 1 + func((x * 3) + 1)
    

print(func(n))