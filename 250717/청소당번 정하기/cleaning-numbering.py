cnt2 = 0
cnt3 = 0
cnt12 = 0

n = int(input())

for i in range(1, n+1):
    if i % 12 == 0:
        cnt12 += 1
    elif i % 3 == 0:
        cnt3 += 1
    elif i % 2 == 0:
        cnt2 += 1

print(cnt2, cnt3, cnt12)

