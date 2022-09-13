#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
16. Дано предложение. Определить число пробелов в нем.
"""

if __name__ == '__main__':
    s = str(input("Введите предложение - "))
    prob = 0
    for i in range(0, len(s)):
        if s[i] == ' ':
            prob += 1
    print("Кол-во пробелов равно - ", prob)