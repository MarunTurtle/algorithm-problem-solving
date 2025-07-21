y, m, d = map(int, input().split())

# Please write your code here.
def is_lunar(y):
    if y % 4 == 0 and y % 100 == 0:
        if y % 400 == 0:
            return True
        else:
            return False
    elif y % 4 == 0:
        return True
    else:
        return False

def which_season(m):
    if 3 <= m <= 5:
        return("Spring")
    elif 6 <= m <= 8:
        return("Summer")
    elif 9 <= m <= 11:
        return("Fall")
    else:
        return("Winter")

def last_day_month(y, m):    
    if m == 2:
        if is_lunar(y):
            return 29
        else:
            return 28
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    else:
        return 31

def day_exist(y, m, d):
    if d <= last_day_month(y, m):
        return True
    else:
        return False

if day_exist(y, m, d):
    print(which_season(m))
else:
    print(-1)
    