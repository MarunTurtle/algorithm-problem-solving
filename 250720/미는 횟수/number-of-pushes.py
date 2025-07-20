str1 = input()
str2 = input()
cnt = 0

while True:
    str1 = str1[-1] + str1[:-1]
    cnt += 1
    if str1 == str2:
        print(cnt)
        break