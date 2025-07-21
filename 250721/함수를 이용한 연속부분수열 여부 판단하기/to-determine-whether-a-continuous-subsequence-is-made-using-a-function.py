import sys

n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def is_sub(i):
    return a[i: i + n2] == b

for i in range(n1 - n2 + 1):
    if is_sub(i):
        print('Yes')
        sys.exit(0)
print('No')