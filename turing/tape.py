#!/usr/env/bin python
"""Class for a Turing machine tape
"""

class Tape():
    """A tape for a turing machine

    Length of tape is only limited by computer memory.
    O(1) lookup and write operations.
    """
    def __init__(self, empty_value='_'):
        self.tape_values = {}
        self.empty_value = empty_value

    def __getitem__(self, index):
        try:
            return self.tape_values[index]
        except KeyError:
            self.tape_values[index] = self.empty_value
            return self.empty_value

    def __setitem__(self, index, value):
        self.tape_values[index] = value

    def format(self, left_bound=None, right_bound=None):
        if left_bound is None:
            try:
                left_bound = min(self.tape_values.keys())
            except ValueError:
                left_bound = 0

        if right_bound is None:
            try:
                right_bound = max(self.tape_values.keys())
            except ValueError:
                right_bound = 0

        return ''.join(
            self[i]
            for i in range(left_bound, right_bound + 1)
        )

    def __str__(self):
        return self.format()

