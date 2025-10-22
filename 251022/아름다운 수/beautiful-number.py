n = int(input())

def is_beautiful(num):
    r = 0
    cur_num = int(str(num)[0])
    for n in str(num):
        x = int(n)
        if cur_num == x:
            r += 1
        else:
            if r % cur_num == 0:
                r = 1
                cur_num = x
            else:
                return False
    return r % cur_num == 0

count = 0

def backtrack(depth, path):
    global count
    if depth == n:
        final = ''.join(map(str, path))
        final = int(final)
        if is_beautiful(final):
            count += 1
            # print(final)
        return

    for i in range(1, 5):
        path.append(i)
        backtrack(depth + 1, path)
        path.pop()

backtrack(0, [])
print(count)