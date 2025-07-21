y = int(input())

# Please write your code here.
def is_lunar(y):
    if y % 100 == 0 and y % 400 != 0:
        return 'false'
    if y % 4 != 0:
        return 'false'
    return 'true'

print(is_lunar(y))