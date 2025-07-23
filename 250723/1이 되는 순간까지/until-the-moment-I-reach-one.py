n= int(input())

# Please write your code here.
count = 0

def func(x):
    global count
    if x == 1:
        return
    count += 1
    if x % 2 == 0:
        func(x//2)
    else:
        func(x//3)

func(n)
print(count)