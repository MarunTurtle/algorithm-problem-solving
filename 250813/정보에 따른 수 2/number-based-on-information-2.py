n, a, b = map(int, input().split())
loc_s = []
loc_n = []

for i in range(n):
    letter, location = tuple(input().split())
    if letter == 'S':
        loc_s.append(int(location))
    else:
        loc_n.append(int(location))

count = 0

for i in range(a, b+1):
    closest_s = 1002
    closest_n = 1002
    
    for s in loc_s:
        closest_s = min(closest_s, abs(s - i))
    for n in loc_n:
        closest_n = min(closest_n, abs(n - i))
    
    if closest_s <= closest_n:
        count += 1

print(count)