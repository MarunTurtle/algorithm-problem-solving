input_str = input()
target_str = input()

# Please write your code here.
input_len = len(input_str)
target_len = len(target_str)
idx = -1

for i in range(input_len - target_len + 1):
    if input_str[i:i+target_len] == target_str:
        idx = i
        print(i)
        break

if idx == -1:
    print(idx)

