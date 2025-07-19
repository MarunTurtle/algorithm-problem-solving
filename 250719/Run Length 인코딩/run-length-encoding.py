A = input()

# Please write your code here.
cnt = 0
curr_letter = ""
ans = ""

for letter in A:
    if letter == curr_letter:
        cnt += 1
    else:
        if cnt > 0:
            ans += f"{curr_letter}{cnt}"
        curr_letter = letter
        cnt = 1
ans += f"{curr_letter}{cnt}"

print(len(ans))
print(ans)


            