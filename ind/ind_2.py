#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дано предложение. Все его символы, стоящие на третьем, шестом, девятом и т. д. местах, заменить буквой а.
"""

if __name__ == '__main__':
    s = str(input("Введите предложение - "))
    schet = 0
    for i in range(0, len(s)):
        if i == schet:
            s[i] = s.replace(s[i], 'a')
        schet += 1
    print(s)