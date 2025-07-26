m1, d1, m2, d2 = map(int, input().split())

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekday = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def count_days(m, d):
    ans = d
    for i in range(1, m):
        ans += days_in_month[i]
    return ans

day_diff = count_days(m2, d2) - count_days(m1, d1)

print(weekday[day_diff % 7])