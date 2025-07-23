n = int(input())

# Please write your code here.

def print_hello(x):
    if x == 0:
        return
    
    print_hello(x-1)
    print('HelloWorld')

print_hello(n)
