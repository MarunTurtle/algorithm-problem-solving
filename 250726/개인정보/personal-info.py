n = 5

class Person:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

persons = []

for i in range(n):
    name, h, w = input().split()
    h, w = int(h), float(w)

    person = Person(name, h, w)
    persons.append(person)

persons.sort(key=lambda x: x.name)
print('name')
for person in persons:
    print(f'{person.name} {person.h} {person.w}')
print()
persons.sort(key=lambda x: -x.h)
print('height')
for person in persons:
    print(f'{person.name} {person.h} {person.w}')