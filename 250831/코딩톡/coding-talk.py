# n 사람 수 / m 메시지 수 / p 확인 번호
# m개의 메시지 - c 메시지 올린 사람, u 아직 읽지 않은 사람
n, m, p = map(int, input().split())
arr = [0] + [tuple(input().split()) for _ in range(m)]
devs = [0] + [arr[i][0] for i in range(1, m+1)]
unreads = [0] + [int(arr[i][1]) for i in range(1, m+1)]
dev_list = [chr(ord('A') + i) for i in range(n)]

for i in range(p, m+1):
    if devs[i] in dev_list:
        dev_list.remove(devs[i])

if unreads[p] == 0:
    print()
else:
    print(*dev_list)