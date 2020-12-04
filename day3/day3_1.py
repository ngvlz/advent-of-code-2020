def tree_encountered(slope_x, slope_y):
    map = []
    x = 0
    tree = 0
    with open('input') as _input:
        for line in _input:
            line = line.rstrip("\n")
            square = list(line)
            map.append(square)
    map = map[::slope_y]
    
    for row in map:
        if row[x] == "#":
            tree+=1 
        x+=slope_x
        if x >= len(row):
            x = x - len(row)
    return(tree)

print("Tree encountered:",tree_encountered(3, 1))
