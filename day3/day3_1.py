map = list()

with open('input') as _input:
    for line in _input:
        line = line.rstrip()
        square = list(line)
        map.append(square)

x = 0
tree = 0

for row in map:
    if row[x] == "#":
        tree+=1 
        print(f"at {x}, hello {tree} tree")
    x+=3
    if x >= len(row):
        x = x - len(row)

print(tree)
