a, b, c = map(int, input().split())

# Please write your code here.

num = a * b * c
    
def func(x):
    if x < 10:
        return x
    return x % 10 + func(x//10)

print(func(num))