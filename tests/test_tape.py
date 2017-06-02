#!/usr/env/bin python
# -*- coding: utf-8 -*-
from nose.tools import assert_equal

from turing.tape import Tape


EMPTY_VALUE = '_'


class TestTape():
    def setUp(self):
        self.tape = Tape()

    def test_init(self):
        tape = Tape()
        assert_equal(tape.tape_values, {})
        assert_equal(tape.empty_value, EMPTY_VALUE)

    def test_write(self):
        tape = Tape()
        for i in range(10):
            tape[i] = chr(i)

    def test_read(self):
        tape = Tape()
        for i in range(10):
            tape[i] = chr(i)

        for i in range(10):
            assert_equal(tape[i], chr(i))

    def test_read_empty(self):
        tape = Tape()
        for i in range(10):
            assert_equal(tape[i], EMPTY_VALUE)

    def test_clear(self):
        tape = Tape()

        for i in range(10):
            tape[i] = chr(i)

        for i in range(20):
            tape[i] = EMPTY_VALUE
