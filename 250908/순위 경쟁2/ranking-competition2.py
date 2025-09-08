n = int(input())
count = 0
a = 0
b = 0
prev_winner = 0

for i in range(n):
    player, score = input().split()
    score = int(score)
    if player == 'A':
        a += score
    else:
        b += score
    
    if cur_winner != prev_winner:
        count += 1
        prev_winner = cur_winner

print(count)
