input_str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

# Please write your code here.
def pull(source):
    return source[1:] + source[0]

def push(source):
    return source[-1] + source[0:-1]

def flip(source):
    for i in range(len(source) // 2):
        source = list(source)
        temp = source[i]
        source[i] = source[len(source)-1-i]
        source[len(source)-1-i] = temp
    return ''.join(source)

for query in queries:
    if query == 1:
        input_str = pull(input_str)
        print(input_str)
    if query == 2:
        input_str = push(input_str)
        print(input_str)
    if query == 3:
        input_str = flip(input_str)
        print(input_str)