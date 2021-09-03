# Solutions

## Puzzle 1

The initialization program (your puzzle input) can either update the bitmask or write a value to memory. Values and memory addresses are both 36-bit unsigned integers. For example, ignoring bitmasks for a moment, a line like mem[8] = 11 would write the value 11 to memory address 8.

The bitmask is always given as a string of 36 bits, written with the most significant bit (representing 2^35) on the left and the least significant bit (2^0, that is, the 1s bit) on the right. The current bitmask is applied to values immediately before they are written to memory: a 0 or 1 overwrites the corresponding bit in the value, while an X leaves the bit in the value unchanged.

## Question 1

Execute the initialization program. What is the **sum of all values** left in memory after it completes?

## Puzzle 2

A version 2 decoder chip doesn't modify the values being written at all. Instead, it acts as a memory address decoder. Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the destination memory address in the following way:

If the bitmask bit is `0`, the corresponding memory address bit is `unchanged`.
If the bitmask bit is `1`, the corresponding memory address bit is `overwritten with 1`.
If the bitmask bit is `X`, the corresponding memory address bit is `floating`.
A floating bit is not connected to anything and instead fluctuates unpredictably. In practice, this means the floating bits will take on all possible values, potentially causing many memory addresses to be written all at once!

## Question 2

Execute the initialization program using an emulator for a version 2 decoder chip. What is the **sum of all values** left in memory after it completes?

## Source

[Advent of Code 2020 Day 15](https://adventofcode.com/2020/day/15 "AoC 2020 Day 15")