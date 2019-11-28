class Person:

    def __init__(self, name, dob=False, address=False):
        self.name = name
        self.dob = dob
        self.address = address

    def __repr__(self):
        return str(self.name)


name_1 = "Javan"
name_2 = "Connor"
name_3 = "Andy"
name_4 = "Chris"
name_5 = "Ife"

unsorted_people = [
    Person(name=name_1),
    Person(name=name_2),
    Person(name=name_3),
    Person(name=name_4),
    Person(name=name_5)
]

print(unsorted_people)
def sort_list(unsorted_people):
    sorted_list = []
    for per in unsorted_people:
        sorted_list.append(per)
    return sorted_list

x = sort_list(unsorted_people)
x.sort()
print(x)