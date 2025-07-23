n = int(input())

# Please write your code here.

def print_number(x):
    if x == 0:
        return

    print(x, end=" ")
    print_number(x-1)

def print_number_reverse(x):
    if x == 0:
        return
    print_number_reverse(x-1)
    print(x, end=" ")

print_number_reverse(n)
print()
print_number(n)
