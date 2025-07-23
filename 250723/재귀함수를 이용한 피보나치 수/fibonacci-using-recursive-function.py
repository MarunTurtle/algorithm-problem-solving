n = int(input())

# Please write your code here.
def pibonacci(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    
    return pibonacci(x-2) + pibonacci(x-1)

print(pibonacci(n))
