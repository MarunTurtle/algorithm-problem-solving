n = int(input())

# Please write your code here.

def print_star(x):
    if x == 0:
        return 
    
    print_star(x-1)
    print('*' * x, end="")
    print()

print_star(n)