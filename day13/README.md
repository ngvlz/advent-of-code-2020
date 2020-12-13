# Solutions

## Puzzle 1

Bus schedules are defined based on a timestamp that measures the number of minutes since some fixed reference point in the past. Each bus has an ID number that indicates how often the bus leaves for the airport.

### Example 1

- Bus ID `5` departs at timestamps `0`, `5`, `10`, `15`, ...

- Bus ID `11` departs at timestamps `0`, `11`, `22`, `33`, ...

### Question 1

Your puzzle input consist of **two lines**.

- The *first line* is your estimate of the **earliest timestamp** you could depart on a bus.
  
- The *second line* lists the **bus IDs** that are in service according to the shuttle company.

- Entries that show `x` must be out of service, so ignore them.

To save time once you arrive, your goal is to figure out the earliest bus you can take to the airport.

What is the ID of the earliest bus you can take to the airport **multiplied by** the number of minutes you'll need to wait for that bus?

## Puzzle 2

The first line in your input is no longer relevant.

Find the earliest timestamp such that the first bus ID departs at that time and each subsequent listed bus ID departs at that subsequent minute.

### Example 2

`7,13,x,x,59,x,31,19`

Find the earliest **timestamp** (called `t`) such that:

- Bus ID `7` departs at timestamp `t`.
  
- Bus ID `13` departs one minute after timestamp `t`.

- There are no requirements or restrictions on departures at two or three minutes after timestamp `t`.

- Bus ID `59` departs four minutes after timestamp `t`.

- There are no requirements or restrictions on departures at five minutes after timestamp `t`.

- Bus ID `31` departs six minutes after timestamp `t`.

- Bus ID `19` departs seven minutes after timestamp `t`.

The **earliest timestamp** at which this occurs is `1068781`.

### Question 2

With the same puzzle input, what is the **earliest timestamp** such that all of the listed bus IDs depart at offsets matching their positions in the list?

## Source

[Advent of Code 2020 Day 13](https://adventofcode.com/2020/day/13 "AoC 2020 Day 13")
