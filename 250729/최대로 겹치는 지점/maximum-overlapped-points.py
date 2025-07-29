MAX_R = 100

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
checked = [0] * MAX_R + 1

def check_box(x, y):
    global checked
    for i in range(x, y+1):
        checked[i] += 1

for a, b in segments:
    check_box(a, b)

print(max(checked))