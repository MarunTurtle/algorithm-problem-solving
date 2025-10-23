n = 6
expression = input()
num = [0 for _ in range(n)]
ans = float('-inf')

def conv(idx):
    return num[ord(expression[idx]) - ord('a')]

def calc():
    l = len(expression)
    total = conv(0)

    for i in range(2, l, 2):
        if expression[i-1] == "-":
            total -= conv(i)
        elif expression[i-1] == '*':
            total *= conv(i)
        else:
            total += conv(i)
    
    return total

def find_max(cnt):
    global ans

    if cnt == n:
        ans = max(ans, calc())
        return
    
    for v in range(1, 5):
        num[cnt] = v
        find_max(cnt + 1)

find_max(0)
print(ans)