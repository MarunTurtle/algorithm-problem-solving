m1, d1, m2, d2 = map(int, input().split())

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

date1 = d1
date2 = d2

for i in range(1, m1):
    date1 += days_in_month[i]

for i in range(1, m2):
    date2 += days_in_month[i]

print(date2 - date1 + 1)
