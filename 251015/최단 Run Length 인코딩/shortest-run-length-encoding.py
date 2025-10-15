a = input()
n = len(a)
# Please write your code here.

def shift(a):
    end = a[-1]
    a = end + a[:n-1]
    return a

def get_run_length(a):
    cur_char = a[0]
    q = 1
    code = cur_char
    for i in range(1, n):
        if a[i] == cur_char:
            q += 1
        else:
            cur_char = a[i]
            code += str(q) + cur_char
            q = 1
    code += str(q)
    return len(code)

ans = get_run_length(a)

for i in range(n-1):
    a = shift(a)
    ans = min(ans, get_run_length(a))

print(ans)