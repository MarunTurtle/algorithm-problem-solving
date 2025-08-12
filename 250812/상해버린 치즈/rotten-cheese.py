p, c, cl, sl = tuple(map(int, input().split()))

cheese_logs = [list(map(int, input().split())) for _ in range(cl)]
sick_logs = [list(map(int, input().split())) for _ in range(sl)]

cheese_logs.sort(key=lambda x : x[2])

poten_sick_people = [0] * (p+1)
toxic_cheese = [0] * (c+1)

for sick_log in sick_logs:
    person = sick_log[0]
    time = sick_log[1]
    for cheese_log in cheese_logs:
        if time > cheese_log[2] and person == cheese_log[0]:
            toxic_cheese[cheese_log[1]] += 1
            poten_sick_people[cheese_log[0]] = 1
# print(toxic_cheese)
# print(poten_sick_people)
for cheese_log in cheese_logs:
    if toxic_cheese[cheese_log[1]] == len(sick_logs):
        poten_sick_people[cheese_log[0]] = 1
# print(poten_sick_people)


ans = poten_sick_people.count(1)

print(ans)