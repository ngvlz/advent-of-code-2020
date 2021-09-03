with open('input', 'r') as program:
    nlist = program.read()
    nlist = nlist.split(',')
    nlist = list(map(int, nlist))

def find_next_number(number_list, target_number):
    number_dict = {}
    for idx, n in enumerate(nlist):
        number_dict[n] = idx + 1

    turn = len(number_dict) + 1
    next_number = 0

    while turn < target_number:
        if next_number in number_dict:
            number_age = turn - number_dict[next_number]
        else:
            number_age = 0

        number_dict[next_number] = turn
        next_number = number_age
        turn += 1
    return next_number

print("Part 1 | The 2020th number is:",find_next_number(nlist, 2020))
print("Part 2 | The 30000000th number is:",find_next_number(nlist, 30000000))