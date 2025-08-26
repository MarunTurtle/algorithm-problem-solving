import itertools

nums = list(map(int, input().split()))
nums.sort()

def contain_all(num_list, test):
    for x, y in list(itertools.combinations(num_list, 2)):
        if x + y in test:
            test.remove(x+y)
        else:
            return False
    for x, y, z in list(itertools.combinations(num_list, 3)):
        if x + y + z in test:
            test.remove(x+y+z)
        else:
            return False
    return True

# a, b, c, d
# a + b, b + c, c + d, d + a, a + c, b + d
# a + b + c, a + b + d, a + c + d, b + c + d
# a + b + c + d
for i in range(11):
    for j in range(i+1, 12):
        for k in range(j+1, 13):
            for l in range(k+1, 14):
                test = nums[:14]
                a = nums[i]
                b = nums[j]
                c = nums[k]
                d = nums[l]
                test.remove(a)
                test.remove(b)
                test.remove(c)
                test.remove(d)
                if nums[14] != a + b + c + d:
                    continue
                if not contain_all([a, b, c, d], test):
                    continue
                print(a, b, c, d)
                break

