n = int(input())
numbers = list(map(int, input().split()))

even = sum(1 for x in numbers if x % 2 == 0)
odd = n - even

count = 0
turn = 0  # 0 = 짝수 차례, 1 = 홀수 차례

while True:
    if turn == 0:  # 짝수 차례
        if even > 0:
            even -= 1
        elif odd >= 2:
            odd -= 2
        else:
            break
    else:  # 홀수 차례
        if odd > 0:
            odd -= 1
        else:
            break
    count += 1
    turn ^= 1  # 짝↔홀 토글

# 마무리: 홀수 하나만 남으면 마지막 두 묶음을 합쳐야 함
if odd == 1:
    count -= 1

print(count)
