MAX_K = 100000
# 변수 선언 및 입력:
n = int(input())
a = [0] * (2 * MAX_K + 1)
cnt_b = [0] * (2 * MAX_K + 1)
cnt_w = [0] * (2 * MAX_K + 1)
b, w, g = 0, 0, 0

cur = MAX_K
for _ in range(n):
    x, c = tuple(input().split())
    x = int(x)

    if c == 'L':
        # x칸 왼쪽으로 칠합니다.
        while x > 0:
            a[cur] = 1
            cnt_w[cur] += 1
            x -= 1

            if x: 
                cur -= 1
    else:
        # x칸 오른쪽으로 칠합니다.
        while x > 0:
            a[cur] = 2
            cnt_b[cur] += 1
            x -= 1

            if x: 
                cur += 1

for i in range(2 * MAX_K + 1):
    # 검은색과 흰색으로 두 번 이상 칠해진 타일은 회색입니다.
    if cnt_b[i] >= 2 and cnt_w[i] >= 2: 
        g += 1
    # 그렇지 않으면 현재 칠해진 색깔이 곧 타일의 색깔입니다.
    elif a[i] == 1: 
        w += 1
    elif a[i] == 2: 
        b += 1

# 정답을 출력합니다.
print(w, b, g)
