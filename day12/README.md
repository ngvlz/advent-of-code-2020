# Solutions

## Puzzle 1

The navigation instructions (puzzle input) consists of a sequence of **single-character actions** paired with **integer input values**.

- `N` ==> move `north` by the given value.
- `S` ==> move `south` by the given value.
- `E` ==> move `east` by the given value.
- `W` ==> move `west` by the given value.
- `L` ==> turn `left` the given number of degrees.
- `R` ==> turn `right` the given number of degrees.
- `F` ==> move `forward` by the given value in the direction the ship is currently facing.

The ship starts by facing `east`. Only the `L` and `R` actions change the direction the ship is facing. The ship position looks something like `[east 17, north 3]` or `[west 10, south 8]`. **The ship's Manhattan distance** is the sum of the absolute values of its east/west position and its north/south position) from its starting position.

Figure out where the navigation instructions lead. **What is the Manhattan distance between that location and the ship's starting position?**

## Puzzle 2

You have been reading the instruction wrong. Almost all of the **actions** indicate how to move a **waypoint** which is **relative to the ship's position**:

- `N` ==> move the waypoint `north` by the given value.
- `S` ==> move the waypoint `south` by the given value.
- `E` ==> move the waypoint `east` by the given value.
- `W` ==> move the waypoint `west` by the given value.
- `L` ==> rotate the waypoint around the ship `left` (counter-clockwise) the given number of degrees.
- `R` ==> rotate the waypoint around the ship `right` (clockwise) the given number of degrees.
- `F` ==> move **the ship** forward to the waypoint a number of times equal to the given value.

Figure out where the navigation instructions actually lead. **What is the Manhattan distance between that location and the ship's starting position?**

## Source

[Advent of Code 2020 Day 12](https://adventofcode.com/2020/day/11 "AoC 2020 Day 12")
