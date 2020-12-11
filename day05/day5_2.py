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
    else: #char == 'B' or 'R'
        result = second_half
    return result

def get_seat_id(bp):
    for i in range(len(bp)):
        if i <= 6:
            exec(f"r{i+1} = get_seat_pos(bp[{i}], r{i})")
        if i > 6:
            exec(f"c{i-6} = get_seat_pos(bp[{i}], c{i-7})")
        if i == 9:
            exec(f"id = r{i-2}[0]*8 + c{i-6}[0]")
    exec(f"seat_ids.append(id)")

r0 = list(range(128))
c0 = list(range(8))
seat_ids = []

for bp in bp_list:
    get_seat_id(bp)

def check_id(id_list):
    min_id = min(id_list)
    max_id = max(id_list)
    for x in range(min_id, max_id):
        if x not in id_list:
            return x

print("My seat ID is:",check_id(seat_ids))
