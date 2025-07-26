n, b = map(int, input().split())

def change_digit(x, d):
    ans = []
    while True:
        if x < d:
            ans.append(x)
            break        
        ans.append(x % d)
        x //= d
    return ans

answer = change_digit(n, b)

for digit in answer[::-1]:
    print(digit, end="")

