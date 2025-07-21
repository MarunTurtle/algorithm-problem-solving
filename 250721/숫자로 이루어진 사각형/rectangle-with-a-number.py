n = int(input())

# Please write your code here.
def fun(n):
    cnt = 1

    for i in range(n):
        for j in range(n):
            print(cnt, end=" ")
            if cnt == 9:
                cnt = 1
            else:
                cnt += 1
        print()

fun(n)