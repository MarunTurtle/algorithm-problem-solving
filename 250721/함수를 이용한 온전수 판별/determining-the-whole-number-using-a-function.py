a, b = map(int, input().split())

# Please write your code here.

def is_perfect(x):
    if x % 2 == 0:
        return False
    if x % 10 == 5:
        return False
    if x % 3 == 0 and x % 9 != 0:
        return False
    return True
cnt = 0
for i in range(a, b+1):
    if is_perfect(i):
        cnt += 1

print(cnt)


