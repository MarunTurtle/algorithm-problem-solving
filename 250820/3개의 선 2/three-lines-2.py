import sys

# 입력
n = int(sys.stdin.readline().strip())
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 후보 직선은 "점에 실제로 등장한 값"만 보면 됩니다.
xs = sorted({x for x, _ in points})   # 세로선 후보들: x = c
ys = sorted({y for _, y in points})   # 가로선 후보들: y = c

def cover_with_three_vertical():
    # 세로선 3개로 덮기: x=i, x=j, x=k
    for i in xs:
        for j in xs:
            for k in xs:
                success = True
                for x, y in points:
                    if x == i or x == j or x == k:
                        continue
                    success = False
                    break
                if success:
                    return True
    return False

def cover_with_two_vertical_one_horizontal():
    # 세로선 2 + 가로선 1: x=i, x=j, y=k
    for i in xs:
        for j in xs:
            for k in ys:
                success = True
                for x, y in points:
                    if x == i or x == j or y == k:
                        continue
                    success = False
                    break
                if success:
                    return True
    return False

def cover_with_one_vertical_two_horizontal():
    # 세로선 1 + 가로선 2: x=i, y=j, y=k
    for i in xs:
        for j in ys:
            for k in ys:
                success = True
                for x, y in points:
                    if x == i or y == j or y == k:
                        continue
                    success = False
                    break
                if success:
                    return True
    return False

def cover_with_three_horizontal():
    # 가로선 3개: y=i, y=j, y=k
    for i in ys:
        for j in ys:
            for k in ys:
                success = True
                for x, y in points:
                    if y == i or y == j or y == k:
                        continue
                    success = False
                    break
                if success:
                    return True
    return False

if (cover_with_three_vertical() or
    cover_with_two_vertical_one_horizontal() or
    cover_with_one_vertical_two_horizontal() or
    cover_with_three_horizontal()):
    print(1)
else:
    print(0)
