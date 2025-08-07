n = int(input())
letters = list(input())

# Please write your code here.

cnt = 0

for i in range(n-2):
    if letters[i] == 'C':
        for j in range(i+1, n-1):
            if letters[j] == 'O':
                for k in range(j+1, n):
                    if letters[k] == 'W':
                        cnt += 1

print(cnt)