#!/usr/env/bin python
# -*- coding: utf-8 -*-
"""Implementation of an A-Machine (Turing Machine)
"""
from turing.tape import Tape


class AMachine():
    """A Turing machine
    """

    def __init__(self, program, start_index=0, initial_state='i1', empty_value='_', sigterm='SIGTERM'):
        """Create a new A-Machine

        Args:
            program: instruction dictionary
            start_index: integer index where the head should start
            initial_state: initial state of the A-Machine
            empty_value: the value that the machine's tape will treat as "empty"
            sigterm: the state for which the machine should stop running
        """
        self.program = program

        self.start_index = start_index
        self.index = start_index

        self.initial_state = initial_state
        self.state = initial_state

        self.empty_value = empty_value
        self.tape = Tape(empty_value=empty_value)

        self.sigterm = sigterm

    def run(self, debug=True):
        """Run the program until it reaches the sigterm state

        Args:
            debug: (boolean) run the machine in debug mode, printing each step
        """
        while self.state != self.sigterm:
            self.step(debug=debug)

    def step(self, n=1, debug=True):
        """Run the A-Machine for a predetermined number of steps

        Args:
            n: number of steps to take
            debug: (boolean) run the machine in debug mode, printing each step
        """
        for i in range(n):
            # Don't run if in sigterm state
            if self.state == self.sigterm:
                break

            if debug:
                print(self)

            # read next instruction
            instruction_key = (self.tape[self.index], self.state)
            # update
            self.tape[self.index], step, self.state = self.program[instruction_key]
            # move head
            self.index += 1 if step == '>' else -1

    def reset(self):
        """Reset the A-Machine to its default state.
        """
        self.index = self.start_index
        self.state = self.initial_state
        self.tape = Tape(empty_value=self.empty_value)

    def __str__(self):
        """Return a string representing the current state of the A-Machine
        """
        tapeline = self.tape.format(
            self.index - 10, self.index + 11) + ' : state {}'.format(self.state)
        pointline = ' ' * 10 + '^' + ' ' * 11 + \
            ' : index {}'.format(self.index)

        return tapeline + '\n' + pointline
