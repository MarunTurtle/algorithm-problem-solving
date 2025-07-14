num = 0
target = 25

while num != target:
    num = int(input())
    if num == target:
        print('Good')
    elif num > target:
        print('Lower')
    else:
        print('Higher')
