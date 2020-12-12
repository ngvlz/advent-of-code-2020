with open('input') as data:
    navigation = data.read()
navigation = navigation.split()


## Set compass #########################
compass = ['E','S','W','N']
x = 0
current_direction = compass[x]


## Set ship position ###################
ship_pos = [0, 0]


## Move the ship position ##############
for n in navigation:
    action = n[0]
    value = int(n[1:])
    
    # -- Move according to direction -- #
    if action == 'N':
        ship_pos[1] += value
    if action == 'S':
        ship_pos[1] -= value
    if action == 'E':
        ship_pos[0] += value
    if action == 'W':
        ship_pos[0] -= value
        
    # -- Rotation -- #
    if action == 'R':
        rotation = int(value/90)
        x += rotation
        if x >= len(compass):
            x = x - len(compass)
        current_direction = compass[x]
        
    if action == 'L':
        rotation = int(value/90)
        x -= rotation
        if x < 0:
            x = x + len(compass)
        current_direction = compass[x]

    # -- Move forward base on direction -- #
    if action == 'F':
        if current_direction == 'N':
            ship_pos[1] += value
        if current_direction == 'S':
            ship_pos[1] -= value
        if current_direction == 'E':
            ship_pos[0] += value
        if current_direction == 'W':
            ship_pos[0] -= value


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
