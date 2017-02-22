program = ['cpy 1 a',
           'cpy 1 b',
           'cpy 26 d',
           'jnz c 2',
           'jnz 1 5',
           'cpy 7 c',
           'inc d',
           'dec c',
           'jnz c -2',
           'cpy a c',
           'inc a',
           'dec b',
           'jnz b -2',
           'cpy c b',
           'dec d',
           'jnz d -6',
           'cpy 19 c',
           'cpy 11 d',
           'inc a',
           'dec d',
           'jnz d -2',
           'dec c',
           'jnz c -5']

registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}


def operator_value(operator):
    if operator in registers:
        return registers[operator]
    return int(operator)


if __name__ == '__main__':
    cp = 0
    while cp < len(program):
        instruction = program[cp].split()
        if instruction[0] == 'cpy':
            registers[instruction[2]] = operator_value(instruction[1])
            cp += 1
        elif instruction[0] == 'jnz':
            if operator_value(instruction[1]) != 0:
                cp += operator_value(instruction[2])
            else:
                cp += 1
        elif instruction[0] == 'inc':
            registers[instruction[1]] += 1
            cp += 1
        elif instruction[0] == 'dec':
            registers[instruction[1]] -= 1
            cp += 1

    print(str(registers))
