year = int(input())

def is_lunar(n):
    if (n % 100 == 0) and (n % 400 != 0):
        return False
    elif (n % 4 == 0):
        return True
    else:
       return False

print("true") if is_lunar(year) else print("false")
