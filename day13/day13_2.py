from itertools import zip_longest

with open('input') as data:
    data = data.read()

data = data.split()
data = data[1].split(',')
for i, bus in enumerate(data):
    if bus == 'x':
        data[i] = 0
    else:
        data[i] = int(data[i])


offsets = []
bus_ids = []
for i, bus in enumerate(data):
    if bus != 0:
        offsets += [i]
        bus_ids += [bus]


periodic_met = bus_ids[0]
t = offsets[0]

for (offset, bus_id) in zip_longest(offsets[1:], bus_ids[1:]):
    first_met = None
    while True:
        if (t + offset) % bus_id == 0:
            if first_met is None:
                first_met = t
            else:
                periodic_met = t - first_met
                break
        t += periodic_met

print("Part 2 | Earliest Timestamp:", first_met)