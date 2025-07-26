n = int(input())

class Person:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

persons = []

for i in range(n):
    name, h, w = input().split()
    h, w = int(h), int(w)

    person = Person(name, h, w)
    persons.append(person)

persons.sort(key=lambda x: (x.h, -x.w))
for person in persons:
    print(f'{person.name} {person.h} {person.w}')
