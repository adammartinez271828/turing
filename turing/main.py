#!/usr/bin/env python
"""Run a Turing machine
"""
from tape import Tape

MAX_ITERATIONS = 8
DEFAULT_STATE = 'i1'

FLIPFLOP = {
    ('_', 'i1'): ('X', '>', 'i2'),
    ('X', 'i1'): ('_', '>', 'i2'),
    ('_', 'i2'): ('_', '<', 'i1'),
}

def print_tape(tape, index, state):
    print(
        tape.format(index-10, index+11) + \
        ' : state {}'.format(state)
    )
    print(' ' * 10 + '^' + ' ' * 11 + ': index {}'.format(index))

def run_program(program):
    tape = Tape()
    index = 0
    state = DEFAULT_STATE

    for _ in range(MAX_ITERATIONS):
        # see where we're at
        print_tape(tape, index, state)

        # read next instruction
        instruction_key = (tape[index], state)
        # update
        tape[index], step, state = program[instruction_key]
        # move head
        index += 1 if step == '>' else -1

    print('Final state:')
    print_tape(tape, index, state)

def main():
    print('Running main')
    run_program(FLIPFLOP)

if __name__ == '__main__':
    main()

