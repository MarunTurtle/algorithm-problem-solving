n, m = map(int, input().split())
numbers = [list(map(int, input().split())) for _  in range(m)]

for number in numbers:
    number.sort()

numbers.sort(key=lambda x:(x[0],x[1]))
# print(numbers)

prev = (0, 0)
ans = 0

for number in numbers:
    if number == prev:
        continue
    else:
        count = 0
        for double in numbers:
            if double == number:
                count += 1
        ans = max(count, ans)
        prev = number

print(ans)