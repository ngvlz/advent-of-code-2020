# Solutions

## Puzzle 1

The `charging outlet` output joltage = `0 jolt`

You have a list of all of the joltage adapters in your bag. Each of your joltage adapters is rated for a specific **output joltage** (The input puzzle)

Any given adapters can take an input of `1`, `2`, `3` jolts lower than its rating and still produce its rated output joltage.

Your `device` output joltage = `the highest-rated adapter output joltage` + `3 jolts higher`

If you use every adapter in your bag at once, there will be a distribution of joltage differences between the charging outlet, the adapters, and your device

**What is the number of `1-jolt differences` multiplied by the number of `3-jolt differences`?**

## Puzzle 2

You need to figure out how many different ways the adapters can be arranged. Every arrangement needs to connect the charging outlet to your device

**What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?**

## Source

[Advent of Code 2020 Day 10](https://adventofcode.com/2020/day/10 "AoC 2020 Day 10")
