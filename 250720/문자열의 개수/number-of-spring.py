books = []
cnt = 0

while True:
    a = input()
    if a == '0':
        break
    cnt += 1
    if cnt % 2 == 1:
        books.append(a)
    
print(cnt)
for book in books:
    print(book)