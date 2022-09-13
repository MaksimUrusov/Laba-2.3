#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дано предложение. Определить количество слов:
    * начинающихся с буквы н;
    * оканчивающихся буквой р.
"""


if __name__ == '__main__':
    s = str(input('Введите слово: '))
    n = 0
    p = 0
    for i in range(0, len(s) - 1):
        if s[i] == "н" and (s[i + 1] == ' ' or i == len(s)):
            n += 1
        if s[i] == "р" and (s[i + 1] == ' ' or i == len(s)):
            p += 1
    print("На н - ", n, "\nОканчивающихся на р - ", p)