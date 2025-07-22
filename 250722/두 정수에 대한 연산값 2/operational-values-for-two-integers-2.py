a, b = map(int, input().split())

# Please write your code here.
def modify(x, y):
    if x > y:
        x *= 2
        y += 10
    else:
        x += 10
        y *= 2
    return x, y

a, b = modify(a, b)

print(a, b)