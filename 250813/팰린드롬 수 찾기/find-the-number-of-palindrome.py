x, y = map(int, input().split())

count = 0
# Please write your code here.
for num in range(x, y+1):
    num_to_str = str(num)
    if num_to_str == num_to_str[::-1]:
        count += 1

print(count)