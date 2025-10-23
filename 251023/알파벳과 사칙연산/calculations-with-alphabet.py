expression = list(input())
operators = []
alphabets = []
for ch in expression:
    if ch in "-*+":
        operators.append(ch)
    else :
        alphabets.append(ch)

variants = sorted(set(alphabets))
n = len(variants)
ans = float('-inf')
assign = {}

def calculate(assign_map):
    numbers = [assign_map[ch] for ch in alphabets]

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
        ans = max(ans, calculate(assign))
        return
    
    for i in range(1, 5):
        assign[variants[depth]] = i
        backtrack(depth + 1)
        assign.pop(variants[depth])

backtrack(0)
print(ans)