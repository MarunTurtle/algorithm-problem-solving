n = int(input())
seats = list(map(int, list(input())))
ans = 0

def get_closest(seats):
    seated = []
    ans = len(seats)
    for i in range(len(seats)):
        if seats[i] == 1:
            seated.append(i)
    
    for i in range(1, len(seated)):
        ans = min(ans, seated[i] - seated[i-1])

    return ans

for i in range(len(seats)-1):
    test = seats[:]
    if test[i] == 0:
        test[i] = 1
        for j in range(i+1, len(seats)):
            if test[j] == 0:
                test[j] = 1
                dist = get_closest(test)
                # print(i, j, test)
                ans = max(ans, dist)
                test[j] = 0

print(ans)