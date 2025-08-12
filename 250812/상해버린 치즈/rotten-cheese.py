p, c, cl, sl = map(int, input().split())

cheese_logs = [tuple(map(int, input().split())) for _ in range(cl)]  # (person, cheese, time)
sick_logs   = [tuple(map(int, input().split())) for _ in range(sl)]  # (person, sick_time)

# 아픈 사람 목록
sick_people = {person for person, _ in sick_logs}

# 1. 치즈별로 "아프기 전에 먹은 아픈 사람들" 집합 만들기
ate_before_sick = [set() for _ in range(c+1)]

for person, cheese, time in cheese_logs:
    for sick_person, sick_time in sick_logs:
        if person == sick_person and time < sick_time:
            ate_before_sick[cheese].add(person)

# 2. 모든 아픈 사람이 먹은 치즈 찾기
toxic_cheeses = {cheese for cheese in range(1, c+1)
                 if ate_before_sick[cheese] == sick_people}

# 3. 그 치즈를 먹은 사람 전부 찾기
poten_sick_people = {person for person, cheese, _ in cheese_logs
                     if cheese in toxic_cheeses}

print(len(poten_sick_people))
