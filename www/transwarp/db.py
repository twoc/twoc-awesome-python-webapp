#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'cc'

'''
Database operation module.
'''

import logging

# Dict object:
class Dict(dict):
    '''
    Simple dict but support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute empty
    >>> d3 = Dict(('a', 'b', 'c'), (1, 2, 3))
    >>> d3.a
    1
    >>> d3.b
    2
    >>> d3.c
    3
    '''
    def __init__(self, names=(), values=(), **kw):
        super().__init__(**kw)
        for k,v in zip(names,values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(str.format("'Dict' object has no attribute {0}",key))

    def __setattr__(self,  key, value):
        self[key] = value

if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("haha")
    import doctest
    doctest.testmod()
