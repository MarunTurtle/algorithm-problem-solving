n = int(input())
queries = []

for i in range(n):
    queries.append(list(map(int, input().split())))

def parse_int(num):
    parsed_num = []
    for i in range(3):
        parsed_num.append(int(str(num)[i]))

    return parsed_num

count = 0

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if len({i, j, k}) != 3:
                continue

            pos_num = [i, j, k]          # 3, 4, 5
            valid = True

            for l in range(n):          
                s, b = 0, 0
                query = parse_int(queries[l][0]) # 1 2 3
                
                for m in range(3):
                    if pos_num[m] == query[m]:
                        s += 1
                    elif pos_num[m] in query:
                        b += 1
                
                if s != queries[l][1] or b != queries[l][2]:
                    valid = False
                    break

            if valid:
                count += 1

print(count)