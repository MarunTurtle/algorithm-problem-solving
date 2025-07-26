binary = list(input())
decimal_num = 0

for digit in binary:
    decimal_num = decimal_num * 2 + int(digit)

decimal_num *= 17
answer = []

while True:
    if decimal_num < 2:
        answer.append(decimal_num)
        break
    
    answer.append(decimal_num % 2)
    decimal_num //= 2

for digit in answer[::-1]:
    print(digit, end="")