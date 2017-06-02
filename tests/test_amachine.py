#!/usr/env/bin python
# -*- coding: utf-8 -*-
from nose.tools import assert_equal

from turing.amachine import AMachine


TEST_PROGRAM = {
    ('_', 'i1'): ('(', '>', 'i2'),
    ('_', 'i2'): ('1', '>', 'i3'),
    ('_', 'i3'): ('1', '>', 'i4'),
    ('_', 'i4'): ('+', '>', 'i5'),
    ('_', 'i5'): ('1', '>', 'i6'),
    ('_', 'i6'): ('1', '>', 'i7'),
    ('_', 'i7'): ('1', '>', 'i8'),
    ('_', 'i8'): ('1', '>', 'i9'),
    ('_', 'i9'): (')', '>', 's1'),
    ('_', 's1'): ('_', '<', 's1'),
    (')', 's1'): (')', '<', 's1'),
    ('1', 's1'): ('1', '<', 's1'),
    ('+', 's1'): ('1', '>', 's2'),
    ('1', 's2'): ('1', '>', 's2'),
    (')', 's2'): ('_', '<', 's3'),
    ('1', 's3'): (')', '>', 'SIGTERM'),
}


class TestAMachine():
    def test_init(self):
        mach = AMachine(TEST_PROGRAM)

        assert_equal(mach.index, 0)
        assert_equal(mach.state, 'i1')
        assert_equal(mach.tape[mach.index], '_')
        assert_equal(mach.sigterm, 'SIGTERM')

    def test_step(self):
        mach = AMachine(TEST_PROGRAM)
        start_index = mach.index
        start_value = mach.tape[start_index]

        mach.step()

        print(mach.index)

        assert_equal(mach.index, start_index + 1)
        assert_equal(mach.tape[0], '(')
        assert_equal(mach.state, 'i2')

    def test_sigterm(self):
        mach = AMachine(TEST_PROGRAM)
        mach.tape[0], mach.state = ('1', 's3')

        mach.step()

        assert_equal(mach.index, 1)
        assert_equal(mach.state, 'SIGTERM')
        assert_equal(mach.tape[mach.index], '_')

        # stepping again should do nothing
        mach.step()

        assert_equal(mach.index, 1)
        assert_equal(mach.state, 'SIGTERM')
        assert_equal(mach.tape[mach.index], '_')
