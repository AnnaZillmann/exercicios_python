people = [
    {"name": "Harry", "House": "Gryffindor"},
    {"name": "Cho", "House": "Ravenclaw"},
    {"name": "Draco", "House": "Slytherin"}
]

# lambda function replace a intire function where describe 'def f(person): / return person["name"/
# people.sort(key=f)] remembering in dictionary where has the key=value, the "word" and the "meaning".
people.sort(key=lambda person: person["name"])

print(people)