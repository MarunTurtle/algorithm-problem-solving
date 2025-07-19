hospital = [0] * 4

for i in range(3):
    patient = list(map(str, input().split()))
    patient[1] = int(patient[1])

    if patient[0] == 'N' and patient[1] < 37:
        hospital[3] += 1
    elif patient[0] == 'N' and patient[1] >= 37:
        hospital[1] += 1
    elif patient[0] == 'Y' and patient[1] < 37:
        hospital[2] += 1
    else:
        hospital[0] += 1

print(*hospital, end=" ")

if hospital[0] >= 2:
    print('E')