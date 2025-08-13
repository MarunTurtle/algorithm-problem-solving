x, y = map(int, input().split())

# Please write your code here.

def is_interesting(num):
    list_num = list(map(int, list(str(num))))
    digits = [0]*10

    for digit in list_num:
        digits[digit] += 1
    
    if digits.count(1) == 1 and digits.count(0) == 8:
        return True
    else:
        return False

count = 0

for i in range(x, y+1):
    if is_interesting(i):
        count += 1

print(count)