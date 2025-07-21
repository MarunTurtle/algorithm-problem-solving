n = int(input())

# Please write your code here.
def func(n):
    total = 0
    for i in range(1, n+1):
        total += i
    
    return int(total / 10)

print(func(n))