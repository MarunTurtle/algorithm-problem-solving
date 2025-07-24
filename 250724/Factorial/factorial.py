N = int(input())

# Please write your code here.
def factorial(x):
    if x == 1:
        return 1
    
    return x * factorial(x-1)

print(factorial(N))