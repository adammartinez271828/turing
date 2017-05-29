#!/usr/env/bin python
# -*- coding: utf-8 -*-


FLIPFLOP = {
    ('_', 'i1'): ('X', '>', 'i2'),
    ('X', 'i1'): ('_', '>', 'i2'),
    ('_', 'i2'): ('_', '<', 'i1'),
}

INIT = {
    ('_', 'i1'): ('(', '>', 'i2'),
    ('_', 'i2'): ('1', '>', 'i3'),
    ('_', 'i3'): ('1', '>', 'i4'),
    ('_', 'i4'): ('+', '>', 'i5'),
    ('_', 'i5'): ('1', '>', 'i6'),
    ('_', 'i6'): ('1', '>', 'i7'),
    ('_', 'i7'): ('1', '>', 'i8'),
    ('_', 'i8'): ('1', '>', 'i9'),
    ('_', 'i9'): (')', '>', 's1'),
}

ADD = {
    ('_', 's1'): ('_', '<', 's1'),
    (')', 's1'): (')', '<', 's1'),
    ('1', 's1'): ('1', '<', 's1'),
    ('+', 's1'): ('1', '>', 's2'),
    ('1', 's2'): ('1', '>', 's2'),
    (')', 's2'): ('_', '<', 's3'),
    ('1', 's3'): (')', '>', 's4'),
    ('_', 's4'): ('_', '>', 's4'),
}

