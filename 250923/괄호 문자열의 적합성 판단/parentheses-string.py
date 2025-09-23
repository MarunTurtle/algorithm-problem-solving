import sys

str = input()
ans = []

for char in str:
    if char == "(":
        ans.append(char)
    else:
        if len(ans) == 0:
            print('No')
            sys.exit(0)
        else:
            ans.pop()

if len(ans) == 0:
    print('Yes')
else:
    print('No')