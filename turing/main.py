#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Run a Turing machine
"""
from tape import Tape
from programs import \
    FLIPFLOP, \
    INIT, \
    ADD


MAX_ITERATIONS = 8
DEFAULT_STATE = 'i1'


def print_tape(tape, index, state):
    print(
        tape.format(index - 10, index + 11) +
        ' : state {}'.format(state)
    )
    print(' ' * 10 + '^' + ' ' * 11 + ' : index {}'.format(index))


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
    global MAX_ITERATIONS

    print('Running main')

    # MAX_ITERATIONS = 9
    # run_program(FLIPFLOP)
    # MAX_ITERATIONS = 9
    # run_program({**INIT, **{('_', 's1'): ('_', '>', 's1')}})
    MAX_ITERATIONS = 22
    run_program({**INIT, **ADD})


if __name__ == '__main__':
    main()
