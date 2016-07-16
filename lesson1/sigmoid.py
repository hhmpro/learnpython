#!/usr/bin/python
# encoding:utf-8

"""
@author  : hhming
@contact : hhmpro@qq.com
@file    : sigmoid.py
@time    : 16/7/16 下午6:23
"""

from math import e, fabs


def sigmoid(x):
    if fabs(x) <= 1e-16:
        return 0.5
    elif fabs(x) >= 37:
        if x > 0:
            return 1
        else:
            return 0
    else:
        return 1.0/(1 + e**(-1 * x))
