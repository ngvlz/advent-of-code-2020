with open('input') as seat_grid:
    seat_grid = seat_grid.readlines()


for i, row in enumerate(seat_grid):
    seat_grid[i] = seat_grid[i].rstrip('\n')
    seat_grid[i] = list(seat_grid[i])


def check_condition(y, x, w, h):
    conditions = [
        y - 1 >= 0 and x - 1 >= 0 and seat_grid[y-1][x-1] == '#', # NW
        y - 1 >= 0 and seat_grid[y-1][x] == '#', # N
        y - 1 >= 0 and x + 1 < w and seat_grid[y-1][x+1] == '#', # NE
        x + 1 < w and seat_grid[y][x+1] == '#', # E
        y + 1 < h and x + 1 < w and seat_grid[y+1][x+1] == '#', # SE
        y + 1 < h and seat_grid[y+1][x] == '#', # S
        y + 1 < h and x - 1 >= 0 and seat_grid[y+1][x-1] == '#', # SW
        x - 1 >= 0 and seat_grid[y][x-1] == '#', # W
        ]
    total_satified_condition = sum(int(checked) for checked in conditions)
    return total_satified_condition


def check_grid(seat_grid):
    new_grid = []
    w = len(seat_grid[0])
    h = len(seat_grid)
    changed = False
    for y, row in enumerate(seat_grid):
        new_row = []
        for x, col in enumerate(row):
            seat_y = y
            seat_x = x
            if seat_grid[y][x] == 'L' and check_condition(seat_y, seat_x, w, h) == 0:
                new_row += ['#']
                changed = True
            elif seat_grid[y][x] == '#' and check_condition(seat_y, seat_x, w, h) >= 4:
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
print("Part 1 | Seats end up occupied:", total_ocuppied_seats)