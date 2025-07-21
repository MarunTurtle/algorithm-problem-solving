m, d = map(int, input().split())

# Please write your code here.

def does_exist(m, d):
    if m == 2:
        return d <= 28
    elif m <= 7:
        if m % 2 == 1:
            return d <= 31
        if m % 2 == 0:
            return d <= 30
    elif 8 <= m <= 12:
        if m % 2 == 0:
            return d <= 31
        if m % 2 == 1:
            return d <= 30
    else:
        return False

print('Yes') if does_exist(m, d) else print('No')
