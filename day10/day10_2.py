import json

adapter_list = json.loads(open('input.json').read())

adapter_list.append(0)                          # add charging outlet
adapter_list.sort()                             # sort adapter in the bag in order
adapter_list.append(adapter_list[-1] + 3)       # add the device

ways = {}

for i, adapter in enumerate(adapter_list):
    # There is only one way to get to the outlet
    if adapter == 0:
        ways[0] = 1
    else:
        sum_ways = []
        for x in range(i-3, i):
            if (0 <= adapter - adapter_list[x] <= 3):
                sum_ways.append(ways.get(adapter_list[x], 0))
        ways[adapter] = sum(sum_ways)


print("Part 2 | Ways to arrange adapters:",ways[adapter_list[-1]])