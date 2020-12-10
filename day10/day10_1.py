import json

adapter_list = json.loads(open('input.json').read())

adapter_list.append(0)                          # add charging outlet
adapter_list.sort()                             # sort adapter in the bag in order
adapter_list.append(adapter_list[-1] + 3)       # add the device

diffs = dict()

for i in range(len(adapter_list)):
    for x in range(1,4):
        if adapter_list[i] + x in adapter_list:
            diffs[x] = diffs.get(x, 0) + 1
            break

print("Part 1 | Answer:",diffs[1]*diffs[3])