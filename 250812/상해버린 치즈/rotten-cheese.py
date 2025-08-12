p, c, cl, sl = tuple(map(int, input().split()))

cheese_logs = [list(map(int, input().split())) for _ in range(cl)]
sick_logs = [list(map(int, input().split())) for _ in range(sl)]

cheese_logs.sort(key=lambda x : (x[1], x[2]))
# print(cheese_logs)

poten_sick_person = [0] * (p+1)
toxic_cheese = [0] * (c+1)

for sick_log in sick_logs:
    sick_person = sick_log[0]
    sick_time = sick_log[1]
    for cheese_log in cheese_logs:
        person = cheese_log[0]
        cheese = cheese_log[1]
        time = cheese_log[2]
        if sick_person == person and time < sick_time:
            toxic_cheese[cheese] += 1

for cheese_log in cheese_logs:
    person = cheese_log[0]
    cheese = cheese_log[1]
    time = cheese_log[2]

    if toxic_cheese[cheese] == len(sick_logs):
        poten_sick_person[person] = 1

ans = poten_sick_person.count(1)

print(ans)