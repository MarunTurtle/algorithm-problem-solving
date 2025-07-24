import sys

string = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
stack = []
bomb_len = len(bomb)

for ch in string:
    stack.append(ch)
    if ''.join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]

result = ''.join(stack)
print(result if result else "FRULA")
