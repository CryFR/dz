old = [2, 4, 9, 16, 26]
new_for = []
new_map = []
new_generator = []

for element in old:
    new_for.append(element**2)
print(new_for)

new_map = list(map(lambda x: pow(x, 2), old))
print(new_map)

new_generator = [x**2 for x in old]
print(new_generator)
