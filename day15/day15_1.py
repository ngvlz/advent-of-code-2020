with open('input', 'r') as program:
    numbers = program.read()
    numbers = numbers.split(',')
    numbers = list(map(int, numbers))

def find_next_number(number_list):
    next_turn = number_list[-1]
    occ_queue = []

    for idx, no in enumerate(number_list):
        try:
            if no == next_turn:
                occ_queue += [idx]
        except Exception as err:
            print(err)
            pass
        finally:
            if len(occ_queue) == 3:
                del occ_queue[0]
    return occ_queue


while len(numbers) < 2020:
    occ_queue = find_next_number(numbers)
    if len(occ_queue) == 1:
        numbers += [0]
    else:
        next_number = occ_queue[-1] - occ_queue[-2]
        numbers += [next_number]

print("Part 1 | The 2020th number:",numbers[-1])
