numbers = [1, 2, 3, 4, 5, 99, 2600, 300]

print(numbers)
numbers.reverse()
print(numbers)

test = "Let's Party!"

string_list = []
for letter in test:
    string_list.append(letter)
print(string_list)
string_list.reverse()
print(string_list)

new_string =""
for letter in string_list:
        new_string += letter
print(new_string)

fellowship_of_the_ring = [
    "Frodo",
    "Sam",
    "Merry",
    "Pippen",
    "Gandalf",
    "Aragorn",
    "Boromir",
    "Legolas",
    "Gimli",
]

print(fellowship_of_the_ring)
if "Gandalf" in fellowship_of_the_ring:
    fellowship_of_the_ring.remove("Gandalf")
    print(fellowship_of_the_ring)
else:
    print("YOU SHALL NOT PASS!")

    