with open('input', 'r') as data:
    # bp = Boarding Pass
    bp_data = data.read() 

bp_list = bp_data.split('\n')

# convert character into seat position
def get_seat_pos(char, id_list):
    middle_idx = len(id_list)//2
    first_half = id_list[:middle_idx]
    second_half = id_list[middle_idx:]
    if char == 'F' or char == 'L':
        result = first_half
    else: #char == 'B' or char == 'R'
        result = second_half
    return result

# get seat ID from input string
# print result of each ID to the screen
def get_seat_id(bp):
    print('-----------------')
    print(bp)
    for i in range(len(bp)):
        if i <= 6:
            exec(f"r{i+1} = get_seat_pos(bp[{i}], r{i})")
            exec(f"if {i} == 6: print('Row:   ', r{i+1})")
        if i > 6:
            exec(f"c{i-6} = get_seat_pos(bp[{i}], c{i-7})")
            exec(f"if {i} == 9: print('Column:',c{i-6})")
        if i == 9:
            exec(f"id = r{i-2}[0]*8 + c{i-6}[0]")
            exec(f"if {i} == 9: print('Seat ID:',id)")
    return exec(f"seat_ids.append(id)")

r0 = list(range(128))
c0 = list(range(8))
seat_ids = []

for bp in bp_list:
    get_seat_id(bp)

# Final answer
print('-----------------\n'
    + 'Max seat ID:',max(seat_ids))
