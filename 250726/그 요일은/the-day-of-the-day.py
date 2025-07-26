m1, d1, m2, d2 = map(int, input().split())
tgt_weekday = input()

weekday = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

tgt_number = weekday.index(tgt_weekday)

def count_days(m, d):
    ans = d
    for i in range(1, m):
        ans += days_in_month[i]
    return ans

answer = 0
start = count_days(m1, d1)
end = count_days(m2, d2)
cur_day = weekday.index('Mon')

for i in range(start, end + 1):  
    if cur_day == tgt_number:  
        answer += 1
    cur_day = (cur_day + 1) % 7

print(answer)