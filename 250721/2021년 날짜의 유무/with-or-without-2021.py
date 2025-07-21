m, d = map(int, input().split())

# Please write your code here.
def last_day_num(m):
    if m == 2:
        return 28
    if m == 4 or m == 6 or m == 9 or m == 1:
        return 30
    return 31

def judge_day(m, d):
    if m <= 12 and d <= last_day_num(m):
        return True
    return False

print('Yes') if judge_day(m, d) else print('No')

