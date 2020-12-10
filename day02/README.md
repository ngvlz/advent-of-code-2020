# Solutions

## Puzzle 1

`num_1 - num_2 a: abcdefgh`

The string (after `:`) must follow the rule (before `:`). The rule is that the given character (to the left of the `:`) must appear at least `num_1` time and at most `num_2` time for the string to be valid

**How many strings are valid** according to the rule?

## Puzzle 2

The new rule indicates that `num_1` and `num_2` are the two positions of the given character in the string (Position in the string start at 1, not 0). **Exactly** one of these positions must contain the character (no more, no less).

**How many strings are valid** according to the new rule?

## Reference

[Advent of Code 2020 Day 2](https://adventofcode.com/2020/day/2 "AoC 2020 Day 2")
