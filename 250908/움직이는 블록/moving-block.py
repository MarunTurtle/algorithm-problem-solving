n = int(input())
blocks = [int(input()) for _ in range(n)]
blocks.sort(reverse=True)
ans = 0

def is_equal():
    prev_block = blocks[0]
    for i in range(1, n):
        if blocks[i] != prev_block:
            return False
    return True

while True:
    if is_equal():
        break
    
    ans += 1
    blocks[0] -= 1
    blocks[n-1] += 1
    blocks.sort(reverse=True)

print(ans)