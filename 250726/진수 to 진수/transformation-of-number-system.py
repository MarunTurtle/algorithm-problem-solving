a, b = map(int, input().split())
binary = list(input())

decimal_num = 0

for digit in binary:
    decimal_num = decimal_num * a + int(digit)

answer = []

while True:
    if decimal_num < b:
        answer.append(decimal_num)
        break
    
    answer.append(decimal_num % b)
    decimal_num //= b

for digit in answer[::-1]:
    print(digit, end="")