m, d = map(int, input().split())

# Please write your code here.

def does_exist(m, d):
    if m == 2 and d <= 28:
        return True
    elif m <= 7:
        if m % 2 == 1:
            if d <= 31:
                return True
        if m % 2 == 0:
            if d <= 30:
                return True
    elif m >= 8:
        if m % 2 == 0:
            if d <= 31:
                return True
        if m % 2 == 1:
            if d <= 30:
                return True
    return False

print('Yes') if does_exist(m, d) else print('No')
