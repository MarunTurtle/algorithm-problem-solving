s1, t1 = map(str, input().split())
s2, t2 = map(str, input().split())
s3, t3 = map(str, input().split())

t1 = int(t1)
t2 = int(t2)
t3 = int(t3)

cnt = 0

patients = [[s1, t1], [s2, t2], [s3, t3]]

for patient in patients:
    if patient[1] >= 37 and patient[0] == 'Y':
        cnt += 1

if cnt >= 2:
    print('E')
else:
    print('N')