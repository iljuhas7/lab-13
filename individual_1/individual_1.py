#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Задание 1
# Выполнить индивидуальное задание лабораторной работы 2.11, оформив все функции программы в виде отдельного модуля.
# Разработанный модуль должен быть подключен в основную программу с помощью одного из вариантов команды import .
# Номер варианта уточнить у преподавателя.

import sys
import commande as cmd


def main():
    while True:
        str_line = cmd.get()

        if str_line == "exit":
            break

        if str_line:
            if cmd.is_name(str_line):
                cmd.call(str_line)

            else:
                print(f"Неизвестная команда {str_line}", file=sys.stderr)


if __name__ == '__main__':
    main()
