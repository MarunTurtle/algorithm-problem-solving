n = int(input())
code1 = list(map(int, input().split()))
code2 = list(map(int, input().split()))

cnt = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            def near(x, y):
                return min(abs(x-y), n - abs(x-y)) <= 2  # 원형 거리 계산

            if (near(i, code1[0]) and near(j, code1[1]) and near(k, code1[2])) \
               or (near(i, code2[0]) and near(j, code2[1]) and near(k, code2[2])):
                cnt += 1

print(cnt)
