n = int(input())
c, s = [], []

hall_of_fame = set(['a', 'b', 'c'])
count = 0

cur_scores = [0, 0, 0]

for i in range(n):
    player, score = input().split()
    score = int(score)

    if player == 'A':
        cur_scores[0] += score
    elif player == 'B':
        cur_scores[1] += score
    else:
        cur_scores[2] += score
    
    max_point = max(cur_scores)
    cur_winner = []

    for i in range(3):
        if cur_scores[i] == max_point:
            cur_winner += chr(97 + i)
    
    if set(cur_winner) != hall_of_fame:
        count += 1
        hall_of_fame = set(cur_winner)

print(count)
    
    


