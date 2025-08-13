x, y = map(int, input().split())
max_sum = 0

# for num in range(x, y+1):
#     num_listed = list(map(int, list(str(num))))
#     max_sum = max(max_sum, sum(num_listed))

# print(max_sum)


def digit_sum(n):
    if n < 10:
        return n
    else:
        return digit_sum(n // 10) + (n % 10)

for i in range(x, y+1):
    max_sum = max(max_sum, digit_sum(i))

print(max_sum)