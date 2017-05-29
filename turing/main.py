#!/usr/bin/env python
"""Run a Turing machine
"""

TAPE_LENGTH = 4
DEFAULT_STATE = 'i1'
ITERATIONS = 6

FLIPFLOP = {
    ('B', 'i1'): ('X', 'R', 'i2'),
    ('X', 'i1'): ('B', 'R', 'i2'),
    ('B', 'i2'): ('B', 'L', 'i1'),
}

def print_tape(tape, index, state):
    print(''.join(tape) + ' : ' + state)
    print(' ' * index + '^')

def run_program(program):
    tape = ['B'] * TAPE_LENGTH
    index = 0
    state = DEFAULT_STATE

    print_tape(tape, index, state)

    for _ in range(ITERATIONS):
        instruction_key = (tape[index], state)
        tape[index], step, state = program[instruction_key]
        index += 1 if step == 'R' else -1

        print_tape(tape, index, state)

def main():
    print('Running main')
    run_program(FLIPFLOP)

if __name__ == '__main__':
    main()

