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


def add(a,b):
    return a + b


def multiply(a,b):
    return a * b


if __name__ == '__main__':
    # a = 10
    # b = '''
    # hello
    # hello
    # hello
    # hello
    # '''
    # c, d, e = 10, 'hello', True
    # print b
    # print c, d, e
    # c, d = d, c
    # print c, d, e
    a = 10
    b = 3
    # print a*1.0/b, a%b, a//b, a**b
    y = a > 3 and b < 4
    z = a > 13 or b <2
    print y, z
