import re

with open("input", 'r') as data:
    __input__ = data.read()

rules = __input__.split("\n")
# l = list
l = {}
bag_l = []

for r in rules:
    r = r.strip(".")
    r = re.sub(" bags| bag|\d |", "", r)
    l[re.split(" contain ", r)[0]] = re.split(" contain ", r)[1].split(", ")


def find_bag(value, l):
    if "shiny gold" in l[value]:
        return True
    else:
        for i in l[value]:
            if i == "no other":
                pass
            else:
                if find_bag(i, l):
                    return True

                
for value in list(l.keys()):
    if find_bag(value, l) == True and value not in bag_l:
        bag_l.append(value)

print("Answer:",len(bag_l))
