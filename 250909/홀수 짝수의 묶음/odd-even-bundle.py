n = int(input())
numbers = list(map(int, input().split()))

even = 0
odd = 0
even_or_odd = 0
count = 0

for i in range(n):
    if numbers[i] % 2 == 0:
        even += 1
    else:
        odd += 1

while even > 0 or odd > 0:
    if even == 1 and odd == 0 and even_or_odd == 1:
        even -= 1
        break
    elif even == 0 and odd == 1 and even_or_odd == 0:
        odd -= 1
        count -= 1
        break
    elif even == 0 and odd == 2:
        if even_or_odd == 0:
            odd -= 2
            count += 1
            break
        elif even_or_odd == 1:
            odd -= 2
            break

    if even_or_odd == 0:
        if even > 0:
            even -= 1
            count += 1
            even_or_odd = 1 - even_or_odd
        elif odd >= 2:
            odd -= 2
            count += 1
            even_or_odd = 1 - even_or_odd
    elif even_or_odd == 1:
        if odd > 0: 
            odd -= 1
            count += 1
            even_or_odd = 1 - even_or_odd


print(count)