# Solutions

## Puzzle 1

Input is the layout of seats. For each seat, consider eight immediate adjacent seats (Like a king on the chess board) and apply these rules:

- `L` means empty seat. If a seat is empty (`L`) and there are **no** occupied seats adjacent to it, the seat becomes occupied.
- `#` means occupied seat. If a seat is occupied (`#`) and **four or more** seats adjacent to it are also occupied, the seat becomes empty.
- `.` means the floor.
- Seats matching no rule don't change. Floor never changes. Seats don't move. Nobody sits on the floor.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. **How many seats end up occupied?**

## Puzzle 2

Instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions (Like a queen on the chess board) and apply these rules:

- Empty seat `L` that see no occupied seats become occupied.
- Occupied seat `#` now takes five or more visible occupied seats to become empty.
- Seats matching no rule don't change. Seats don't move.
- Floor `.` never changes. Nobody sits on the floor.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. **How many seats end up occupied?**

## Source

[Advent of Code 2020 Day 11](https://adventofcode.com/2020/day/11 "AoC 2020 Day 11")
