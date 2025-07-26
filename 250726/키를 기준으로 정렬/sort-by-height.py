n = int(input())

persons = []

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


for i in range(n):
    name, height, weight = input().split()

    person = Person(name, height, weight)

    persons.append(person)

persons.sort(key=lambda x:x.height)

for person in persons:
    print(f'{person.name} {person.height} {person.weight}')
