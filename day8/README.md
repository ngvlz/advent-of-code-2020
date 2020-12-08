# Solutions

## Puzzle 1

The boot code is represented as a text file with one instruction per line of text. 

Each instruction consists of an **operation** (`acc`, `jmp`, or `nop`) and an **argument** (a signed number like `+4` or `-20`).

- `acc` increases or decreases a single global value called the `accumulator` (starting at 0) by the value given in the argument.

  After an `acc` instruction, the instruction immediately below it is executed next.

- `jmp` jumps to a new instruction relative to itself. 
  
  The next instruction to execute is found using the argument as an offset from the jmp instruction

- `nop` stands for No OPeration - it does nothing. 
  
  The instruction immediately below it is executed next.

The original boot code is an `infinite loop`.

Before any instruction is executed a second time, **what value is in the accumulator?**

## Puzzle 2

By changing exactly **one** `jmp` (to `nop`) or `nop` (to `jmp`), fix the program.

**What is the value of the accumulator after the program terminates normally?**
