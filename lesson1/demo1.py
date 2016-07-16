#!/usr/bin/python
# encoding:utf-8

"""
@author  : hhming
@contact : hhmpro@qq.com
@file    : demo2.py
@time    : 16/7/16 下午3:02
"""


def hello():
    print 'I am in demo1'

if __name__ == '__main__':
    a = 10
    b = '''
    hello
    hello
    hello
    hello
    '''
    c, d, e = 10, 'hello', True
    print b
    print c, d, e
    c, d = d, c
    print c, d, e
