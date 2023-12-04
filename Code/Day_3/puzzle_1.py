import more_itertools as mit
file = open("engine_schematic.txt", "r")
rows = file.readlines()
# stuff =  if (not c.isalnum() and (c != "." and c != r"\n")
part_number = ""
part_numbers = []
char_pos = []
num_pos = []
for i in range(len(rows)):
    row = rows[i]
    row = row.replace(r"\n", "")
    for j in range(len(row)):
        character = row[j]
        if not character.isalnum() and character != ("." or "\n") and j != 140:
            char_pos.append((i * 140) + (j + 1))
        if character.isnumeric() and j != 140:
            num_pos.append((i * 140) + (j + 1))

current_number_index = 0
current_number = []
templist = []
part_number_indexes = []
for i in range(len(num_pos)):
    x = num_pos[i]
    adjacent_indexes = [x - 141, x - 140, x - 139, x - 1, x + 1, x + 139, x + 140, x + 141]
    for index in adjacent_indexes:
        if index in char_pos:
            templist.append(x)

temp2 = []
num_pos = [list(group) for group in mit.consecutive_groups(num_pos)]
for i in num_pos:
    if any(j for j in i if j in templist):
        temp2.append(i)


print(temp2)

for i in temp2:
    for j in i:
        print((j % 141) - 1)

