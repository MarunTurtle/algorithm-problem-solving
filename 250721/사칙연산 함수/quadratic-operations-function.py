a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def get_prod(x, y):
    return f"{x} * {y} = {x * y}"

def get_sum(x, y):
    return f"{x} + {y} = {x + y}"

def get_quotient(x, y):
    return f"{x} / {y} = {x // y}"

def get_diff(x, y):
    return f"{x} - {y} = {x - y}"

if o == "+":
    print(get_sum(a, c))
elif o == '-':
    print(get_diff(a, c))
elif o == '*':
    print(get_prod(a, c))
elif o == '/':
    print(get_quotient(a, c))
else:
    print(False)