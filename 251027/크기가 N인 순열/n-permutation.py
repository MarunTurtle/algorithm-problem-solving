n = int(input())

# Please write your code here.
selected = []
visited = [False] * (n+1)

def get_combination(depth):
    if depth == n:
        print(*selected)
        return

    for i in range(1, n+1):
        if not visited[i]:
            selected.append(i)  
            visited[i] = True   
            get_combination(depth + 1)
            selected.pop()
            visited[i] = False

get_combination(0)
