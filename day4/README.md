# Solutions

## Puzzle 1

Required field on a valid passport:

- `byr`: Birth Year

- `iyr`: Issue Year

- `eyr`: Expiration Year

- `hgt`: Height

- `hcl`: Hair Color

- `ecl`: Eye Color

- `pid`: Passport ID

- `cid`: Country ID (only this field is optional)

Valid passport has all those fields present in it (with `cid` optional). **How many passports are valid?**

## Puzzle 2

- `byr` (Birth Year): 4 digits; 1920 <= x <= 2002.

- `iyr` (Issue Year) - 4 digits; 2010 <= x <= 2020.

- `eyr` (Expiration Year) - 4 digits; 2020 <= x <= 2030.

- `hgt` (Height) - a number followed by either `cm` or `in`:

  - If `cm`, the number must be 150 <= x <= 193.

  - If `in`, the number must be 59 <= x >= 76.

- `hcl` (Hair Color) - a # followed by *exactly* 6 characters 0-9 or a-f.

- `ecl` (Eye Color) - exactly one of: `amb` `blu` `brn` `gry` `grn` `hzl` `oth`.

- `pid` (Passport ID) - a 9-digit number, including leading 0s.

- `cid` (Country ID) - *ignored*, missing or not.

*Note*: `x` is a placeholder

Valid passport has all the required fields with valid values. **How many passports are valid?**

## Source

[Advent of Code 2020 Day 4](https://adventofcode.com/2020/day/4 "AoC 2020 Day 4")
