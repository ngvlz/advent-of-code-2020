# Solutions

## Puzzle 1

A seat is specified with letter format, such as `FBFFBBFLRL`,
where `F` means "front", `B` means "back", `L` means "left", and `R` means "right".

The first 7 characters specify the row number. They are either `F` or `B`.

The last 3 characters are specified the column number. They are either `L` or `R`

There are `128` rows (from `0` to `127`) and `8` columns (from `0` to `7`)

Each letter in the seat texts tells with half of a region the given seat is in:

`F`: The lower half

`B`: The upper half

`L`: The lower half

`R`: The upper half

Enumerate through the texts until there is exactly one row and one seat left --> That is the given seat position

Seat ID = `row position * 8 + column position`

Check through the list of boarding passes. **What is the highest Seat ID on the boarding pass?**

## Puzzle 2

Your seat is the only missing boarding pass in your list.

Seats at the very front and very back don't exist, which means they are not in the list of boarding passes.

The seat with IDs `+ 1` and `- 1` from your seat will be in the boarding pass. **What is your Seat ID?**

## Source

[Advent of Code 2020 Day 5](https://adventofcode.com/2020/day/5 "AoC 2020 Day 5")
