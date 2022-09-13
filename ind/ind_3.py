#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дано слово. Переставить его первую букву на место -й. При этом вторую, третью, ..., -ю
буквы сдвинуть влево на одну позицию.
"""

if __name__ == '__main__':
    w = str(input('Введите слово: '))
    k = int(input('Введите k: '))
    tmp = list(w)

    s = tmp[0]
    for i in range(k - 1, len(w) - 1):
        tmp[i] = tmp[i + 1]
    tmp[k - 1] = s

    w = ''.join(tmp)
    print(w)