n = int(input())

cnt = 0

for i in range(n):
    scores = list(map(int, input().split()))
    if sum(scores) // len(scores) >= 60:
        print("pass")
        cnt += 1
    else:
        print('fail')
print(cnt)