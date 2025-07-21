a, b = map(int, input().split())

# Please write your code here.
def tsn(x):
    if '3' in str(x) or '6' in str(x) or '9' in str(x):
        return True
    else:
        return False

def tm(x):
    if x % 3 == 0:
        return True
    else:
        return False

cnt = 0
for i in range(a, b+1):
    if tsn(i) or tm(i):
        cnt += 1

print(cnt)