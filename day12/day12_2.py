with open('input') as data:
    navigation = data.read()
navigation = navigation.split()


## Set waypoint position ###############
waypoint = [10, 1]


## Set ship position ###################
ship_pos = [0, 0]


## Move waypoint and ship ##############
for n in navigation:
    # -- Set rotation based on the x axis, y axis -- #
    waypoint_rotation = [[waypoint[0], waypoint[1]], [waypoint[1], -waypoint[0]], [-waypoint[0], -waypoint[1]], [-waypoint[1], waypoint[0]]]

    action = n[0]
    value = int(n[1:])
    
    # -- Move waypoint according to direction -- #
    if action == 'N':
        waypoint[1] += value
    if action == 'S':
        waypoint[1] -= value
    if action == 'E':
        waypoint[0] += value
    if action == 'W':
        waypoint[0] -= value

    # -- Rotate waypoint -- #
    if action == 'R':
        rotation = int(value/90)
        waypoint = waypoint_rotation[rotation]
    if action == 'L':
        rotation = -int(value/90)
        waypoint = waypoint_rotation[rotation]

    # -- Move the ship to the waypoint -- #
    if action == 'F':
        ship_pos[0] += waypoint[0]*value
        ship_pos[1] += waypoint[1]*value


## Format output to print ##############
if ship_pos[0] > 0:
    current_x_pos = 'East'
else:
    current_x_pos = 'West'

if ship_pos[1] > 0:
    current_y_pos = 'North'
else:
    current_y_pos = 'South'

ship_pos = [abs(i) for i in ship_pos]


## Print result ########################
print(f"Current position   ==> {current_x_pos} {ship_pos[0]}, {current_y_pos} {ship_pos[1]}")
print("Manhattan distance ==>",sum(ship_pos))
