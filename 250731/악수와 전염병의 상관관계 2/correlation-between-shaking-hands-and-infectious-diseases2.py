class Shake:
    def __init__(self, time, p1, p2):
        self.time = time
        self.p1 = p1
        self.p2 = p2

# n명의 개발자
# k번까지 전염
# p가 전염 시작
# t번 동안 악수 진행
n, k, p, t = map(int, input().split())
shakes = []

developers = [0] * (n + 1)
infect_cnt = [0] * (n + 1)
developers[p] = 1

for i in range(t):
    s, x, y = map(int, input().split())
    shakes.append(Shake(s, x, y))

shakes.sort(key = lambda x: x.time)

for shake in shakes:
    x = shake.p1
    y = shake.p2

    if developers[x] == 1 and developers[y] != 1:
        if infect_cnt[x] < k:
            developers[y] = 1    
        infect_cnt[x] += 1
    elif developers[y] == 1 and developers[x] != 1:
        if infect_cnt[y] < k:
            developers[x] = 1    
        infect_cnt[y] += 1
    elif developers[y] == 1 and developers[x] == 1:
        infect_cnt[x] += 1
        infect_cnt[y] += 1

for i in range(1, n + 1):
    print(developers[i], end="")
