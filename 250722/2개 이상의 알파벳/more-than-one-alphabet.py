a = input()

# Please write your code here.
alpha = []

def count_alpha(a):
    for i in range(len(a)):
        if a[i] not in alpha:
            alpha.append(a[i])

count_alpha(a)

if len(alpha) >= 2:
    print('Yes')
else:
    print('No')