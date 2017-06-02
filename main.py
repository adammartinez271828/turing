#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Run a Turing machine
"""
from turing.amachine import AMachine
from turing.programs import \
    FLIPFLOP, \
    INIT, \
    ADD


def main():
    print('Running main')

    machine = AMachine(FLIPFLOP)
    machine.step(9)

    # machine = AMachine({**INIT, **{('_', 's1'): ('_', '>', 's1')}})
    # machine.step(9)

    # machine = AMachine({**INIT, **ADD})
    # machine.run()


if __name__ == '__main__':
    main()
