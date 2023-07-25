#initialise empty directionary
d = {}
d2 = dict()
#print(type(d2))

#intialising non-emoty dictionary
phonebook = {"Thomas":7676887878, "Ruud":7878665656, "July":8898989877}
#print(phonebook)
#print individual  elements
name = input("who you gonna call")
if name in phonebook:
    print(f"calling...{phonebook[name]}")
else:
    print(f"no number for ...[name]")

#zipping two lists togheter into directionary
names = ["Marius", "Nazaret", "Micheala"]
ages = [23, 22, 21]
people = dict(zip( ages, names))
print(people)
# values could be anything, but key must be immutable

#traversing dictionaries- accesing key/values
for thing in people:
    print(thing)
for thing in people.values():
    print(thing)
for v, k in people.items():
    print(f"person {k} is {v} years old ")