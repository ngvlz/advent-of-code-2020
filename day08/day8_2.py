
with open('input') as data:
    boot_code = data.readlines()


def start_program(boot_code):
    
    acc = 0
    visited_lines = []
    starter_code = boot_code[0]
    code_queue = [(starter_code, 0)]
    
    while code_queue:
        try:
            code = code_queue[0][0] 
            instruction = code.split(" ")[0]
            value = int(code.split(" ")[1])
            
            if code_queue[0][1] in visited_lines:
                return False
            
            if instruction == 'nop':
                next_line = code_queue[0][1] + 1
            if instruction == 'acc':
                acc += value
                next_line = code_queue[0][1] + 1
            if instruction == 'jmp':
                next_line = code_queue[0][1] + value
                
            visited_lines.append(code_queue[0][1])
            code_queue.append((boot_code[next_line], next_line))
            
        except Exception:
            return acc
        
        finally:
            del code_queue[0]


for idx, instruction in enumerate(boot_code):
    
    operator, arg = instruction.split(' ')
    if operator == 'nop':
        operator_fixed = 'jmp'
        boot_code[idx] = f'{operator_fixed} {arg}'
        
    elif operator == 'jmp':
        operator_fixed = 'nop'
        boot_code[idx] = f'{operator_fixed} {arg}'


    output = start_program(boot_code)
    if output is False:
        boot_code[idx] = f'{operator} {arg}'
    else:
        print("Part 2 | Accumulator value:",output)
        break