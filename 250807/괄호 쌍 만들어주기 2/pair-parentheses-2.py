# 변수 선언 및 입력
string = input()
n = len(string)

# 모든 쌍을 다 잡아봅니다.
cnt = 0
for i in range(n - 1):
    for j in range(i + 2, n - 1):
        if string[i] == '(' and string[i + 1] == '(' and string[j] == ')' and string[j + 1] == ')':
            cnt += 1
            
print(cnt)
