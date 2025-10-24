# 변수 선언 및 입력

n, m = tuple(map(int, input().split()))
combination = []

def find_combination(curr_num, cnt):
    if curr_num == n + 1:
        if cnt == m:
            print(*combination)
        return

    combination.append(curr_num)
    find_combination(curr_num + 1, cnt + 1)
    combination.pop()

    find_combination(curr_num + 1, cnt)

find_combination(1, 0)
