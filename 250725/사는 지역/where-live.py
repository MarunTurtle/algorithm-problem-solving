n = int(input())

class Person:
    def __init__(self, name, address_num, location):
        self.name = name
        self.address_num = address_num
        self.location = location
    
persons = []
for _ in range(n):
    name, address_num, location = tuple(input().split())
    person = Person(name, address_num, location)
    persons.append(person)

persons.sort(key=lambda x : x.name)
print(f'name {persons[n-1].name}')
print(f'addr {persons[n-1].address_num}')
print(f'city {persons[n-1].location}')