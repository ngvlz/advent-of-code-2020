slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

def tree_encountered(slope_x, slope_y):
    map = []
    x = 0
    tree = 0
    with open('input') as _input:
        for line in _input:
            line = line.rstrip("\n")
            line = list(line)
            map.append(line)

    map = map[::slope_y]
    
    for row in map:
        if row[x] == "#":
            tree+=1 
        x+=slope_x
        if x >= len(row):
            x = x - len(row)
    return(tree)

def multiply(num_list):
    result = 1
    for num in num_list:
        result *= num
    return result

tree_list = []

for slope in slopes:
    tree_per_slope = tree_encountered(slope[0], slope[1])
    tree_list.append(tree_per_slope)

print(multiply(tree_list))