expression = input()
n = 6
path = [0 for _ in range(n)]
ans = float('-inf')

def conv(alpha):
    return path[ord(expression[i]) - ord('a')] 

def calculate():
    length = len(expression)
    total = conv(0)
    for i in range(2, length, 2):
        if expression[i-1] == '+':
            total += conv(i)
        elif expression[i-1] == '-':
            total -= conv(i)
        else:
            total += conv(i)
    return total

def backtrack(depth):
    global ans

    if depth == n:
        ans = max(ans, calculate())
        return
    
    for i in range(1, 5):
        path[depth] = i
        backtrack(depth + 1)

backtrack(0)
print(ans)
