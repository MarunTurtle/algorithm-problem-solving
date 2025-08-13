x, y = map(int, input().split())

count = 0
# Please write your code here.
for num in range(x, y+1):
    num_to_str = str(num)
    r = len(num_to_str)
    if r % 2 == 0:
        l = len(num_to_str)//2
        left = num_to_str[:l]
        right = num_to_str[l:][::-1]
    else:
        l = (r+1)//2
        left = num_to_str[:l]
        right = num_to_str[l-1:][::-1]
    if left == right:
        count += 1

print(count)