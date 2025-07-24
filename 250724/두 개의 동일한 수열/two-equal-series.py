n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def equal():
    for elem1, elem2 in zip(A, B):
        if elem1 != elem2:
            return False
    return True

# Please write your code here.
A.sort()
B.sort()

if equal():
    print('Yes')
else:
    print('No')