from itertools import zip_longest, product
import re

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

        mem = re.search("\d+", i[0])
        mem = mem.group()
        mem= f"{int(mem):036b}"
        mem = list(mem)
        
        for idx, (value, mask) in enumerate(zip_longest(mem, mask_value)):
            if mask == "0":
                pass
            elif mask == "1":
                mem[idx] = "1"
            elif mask == "X":
                mem[idx] = "X"

        x_idx = []
        for idx, v in enumerate(mem):
            if v == "X":
                x_idx += [idx]

        x_occurence = mem.count("X")
        # Cartesian product of input iterables
        x_combinations = product("01", repeat=x_occurence)
        final_mem = []

        for combination in x_combinations:
            modified_mem = mem
            for (idx, replacement) in zip_longest(x_idx, combination):
                modified_mem[idx] = replacement
            modified_mem = "".join(modified_mem)
            modified_mem = int(modified_mem, 2)
            final_mem += [modified_mem]
        for memory in final_mem:
            memory[f"mem[{memory}]"] = int(i[1])

print("Part 2 | The sum of all values left in memory:",sum(memory.values()))