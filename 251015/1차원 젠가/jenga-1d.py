n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.

def simulate(s, e):
    global blocks

    tmp = []
    for i in range(len(blocks)):
        if s-1 <= i <= e-1:
            continue
        else:
            tmp.append(blocks[i])
    blocks = tmp

simulate(s1, e1)
simulate(s2, e2)

print(len(blocks))
for block in blocks:
    print(block)
