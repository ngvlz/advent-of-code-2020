with open('input') as seat_grid:
    seat_grid = seat_grid.readlines()


for i, row in enumerate(seat_grid):
    seat_grid[i] = seat_grid[i].rstrip('\n')
    seat_grid[i] = list(seat_grid[i])


adjacent_pos = [(-1, -1), (-1, 0), (-1, 1),
                ( 0, -1),          ( 0, 1),
                ( 1, -1), ( 1, 0), ( 1, 1)]
w = len(seat_grid[0])
h = len(seat_grid)


def check_what_can_see(seat_grid, y, x, move_y, move_x):
    y += move_y
    x += move_x
    while (0 <= y < h and 0 <= x < w):
        if seat_grid[y][x] == '#':
            return 1
        if seat_grid[y][x] == 'L':
            return 0
        y += move_y
        x += move_x
    return 0


def check_adjacent_seats(seat_grid, y, x):
    seats_can_be_seen = []
    for (move_y, move_x) in adjacent_pos:
        seen = check_what_can_see(seat_grid, y, x, move_y, move_x)
        seats_can_be_seen.append(seen)
    occupied_seats_in_sight = sum(seats_can_be_seen)
    return occupied_seats_in_sight


def check_grid(seat_grid):
    new_grid = []
    changed = False
    for y, row in enumerate(seat_grid):
        new_row = []
        for x, col in enumerate(row):
            seat_y = y
            seat_x = x
            if seat_grid[y][x] == 'L' and check_adjacent_seats(seat_grid, seat_y, seat_x) == 0:
                new_row += ['#']
                changed = True
            elif seat_grid[y][x] == '#' and check_adjacent_seats(seat_grid, seat_y, seat_x) >= 5:
                new_row += ['L']
                changed = True
            else:
                new_row += [seat_grid[y][x]]
        new_grid += [new_row]
    return new_grid, changed


while True:
    seat_grid, changed = check_grid(seat_grid)
    if not changed:
        break
total_ocuppied_seats = sum(row.count('#') for row in seat_grid)
print("Part 2 | Seats end up occupied:", total_ocuppied_seats)