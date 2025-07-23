n = int(input())

# Please write your code here.

def print_num(x):
    if x == 0:
        return
        
    
    print(x, end=" ")
    print_num(x-1)
    print(x, end=" ")


print_num(n)