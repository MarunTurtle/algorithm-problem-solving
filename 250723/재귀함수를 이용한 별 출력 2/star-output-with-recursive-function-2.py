n = int(input())

# Please write your code here.

def print_stars(x):
    if x == 0:
        return
    
    for i in range(x):
        print('*', end=" ")
    print()
    print_stars(x-1)
    for i in range(x):
        print('*', end=" ")
    print()
    
print_stars(n)