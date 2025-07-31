MAX_T = 250
# n명의 개발자
# k번까지 전염
# p가 전염 시작
# t번 동안 악수 진행
n, k, p, t = map(int, input().split())

developers = [0] * (n + 1)
developers[p] = 1
cnt = 0

time = [(0, 0)] * (MAX_T + 1)

for i in range(t):
    s, x, y = map(int, input().split())
    time[s] = (x, y)

for x, y in time:
    if developers[x] == 1 or developers[y] == 1:
        if cnt < k:
            developers[x] = 1
            developers[y] = 1
            cnt += 1

for i in range(1, n + 1):
    print(developers[i], end="")
