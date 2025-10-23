expression = list(input())
operators = []
alphabets = []
for ch in expression:
    if ch in "-*+":
        operators.append(ch)
    else :
        alphabets.append(ch)

n = len(alphabets)
ans = float('-inf')
path = []

def calculate(numbers):
    total_ans = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i-1] == '-':
            total_ans -= numbers[i]
        elif operators[i-1] == '*':
            total_ans *= numbers[i]
        else:
            total_ans += numbers[i]
    return total_ans

def backtrack(depth):
    global ans

    if depth == n:
        ans = max(ans, calculate(path))
        return
    
    for i in range(1, 5):
        path.append(i)
        backtrack(depth + 1)
        path.pop()      
    
backtrack(0)
print(ans)