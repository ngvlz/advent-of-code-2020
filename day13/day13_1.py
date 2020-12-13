with open('input') as data:
    data = data.read()

data = data.split()
my_depart_t = int(data[0])
data[1] = data[1].split(',')
for i, bus in enumerate(data[1]):
    if bus == 'x':
        data[1][i] = 0
    else:
        data[1][i] = int(data[1][i])


def find_bus(bus_list):
    bus_depart_schedule = []
    for bus_id in bus_list:
        try:
            t = ((my_depart_t//bus_id) + 1) * bus_id
            bus_depart_schedule += [(t, bus_id)]
        except Exception:
            pass

    earliest_bus_t = min([bus[0] for bus in bus_depart_schedule])
    earliest_bus_id = int([bus_id for t, bus_id in bus_depart_schedule if t == earliest_bus_t][0])
    return (earliest_bus_t-my_depart_t)*earliest_bus_id


result = find_bus(data[1])
print("Part 1 | Bus ID x Time wait =", result)
