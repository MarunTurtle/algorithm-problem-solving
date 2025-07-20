str1 = input()
str2 = input()
cnt = 0
trg = len(str1)

while True:
    if str1 == str2:
        print(cnt)
        break
    str1 = str1[-1] + str1[:-1]
    cnt += 1
    if cnt == trg:
        print(-1)
        break