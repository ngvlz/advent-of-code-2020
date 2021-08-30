from itertools import zip_longest

with open('input', 'r') as program:
    program = program.read()
    program = program[7:]
    program = program.split('\nmask = ')

memory = {}

for data in program:
    data = data.split("\n")
    mask_value = data[0]

    for i in data[1:]:
        i = i.split(" = ")
        i[1] = f"{int(i[1]):036b}"
        for idx, (value, mask) in enumerate(zip_longest(i[1], mask_value)):
            if mask != "X":
                i[1] = i[1][:idx] + mask + i[1][idx+1:]
        i[1] = int(i[1], 2)
        memory[i[0]] = i[1]

print("Part 1 | The sum of all values left in memory:",sum(memory.values()))
