MAX_K = 100000
# 변수 선언 및 입력:
n = int(input())
a = [0] * (2 * MAX_K + 1)

b, w = 0, 0

cur = MAX_K
for _ in range(n):
    x, c = tuple(input().split())
    x = int(x)

    if c == 'L':
        # x칸 왼쪽으로 칠합니다.
        while x > 0:
            a[cur] = 1
            x -= 1

            if x: 
                cur -= 1
    else:
        # x칸 오른쪽으로 칠합니다.
        while x > 0:
            a[cur] = 2
            x -= 1

            if x: 
                cur += 1

for i in range(2 * MAX_K + 1):
    if a[i] == 1: 
        w += 1
    if a[i] == 2: 
        b += 1

# 정답을 출력합니다.
print(w, b)
