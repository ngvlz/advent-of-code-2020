import re

with open("input", 'r') as data:
    __input__ = data.read()

rules = __input__.split("\n")

# l = list
l = {}

for r in rules:
    r = r.strip(".")
    r = re.sub(" bags| bag|", "", r)
    containing_bag = re.split(" contain ", r)[0]
    bag_info = re.split(" contain ", r)[1].split(", ")
    for i, bag in enumerate(bag_info):
        if bag == "no other":
            bag_info is None
        else:
            bag_info[i] = bag.split(" ", 1)
            bag_info[i][0] = int(bag_info[i][0])
            
    l[containing_bag] = bag_info

my_bag = "shiny gold"
bag_queue = [(my_bag, 1)]
count = 0

while bag_queue:
    try:
        for bag in l[bag_queue[0][0]]:
            count += bag[0] * bag_queue[0][1]
            bag_queue.append((bag[1], bag[0] * bag_queue[0][1]))
    except TypeError:
        pass
    finally:
        del bag_queue[0]

print("Answer:",count)


