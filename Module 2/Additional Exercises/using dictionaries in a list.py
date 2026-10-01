people = [
    {"Name": "Alice", "Race": "White"},
    {"Name": "Jenny", "Race": "Black"},
    {"Name": "Peter", "Race": "Indian"}
]

print (people)
# Accessing items:
for person in people:
    print(person.values())
    print(person.items())