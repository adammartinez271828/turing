#!/usr/env/bin python
# -*- coding: utf-8 -*-


FLIPFLOP = {
    ('_', 'i1'): ('X', '>', 'i2'),
    ('X', 'i1'): ('_', '>', 'i2'),
    ('_', 'i2'): ('_', '<', 'i1'),
}

