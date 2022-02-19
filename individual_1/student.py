#!/usr/bin/env python3
# -*- coding: utf-8 -*-

students = []


def add():
    name = input("Фамилия и инициалы? ")
    number = input("Номер группы? ")
    z = str(input("Успеваемость? "))

    student = {
        'name': name,
        'number': number,
        'z': z,
    }

    students.append(student)
    if len(student) > 1:
        students.sort(key=lambda item: item.get('name', ''))


def print_line():
    print('+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
    )


def print_list():
    print_line()
    print(
        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "№",
            "Ф.И.О.",
            "Номер группы",
            "Успеваемость"
        )
    )
    print_line()
    for idx, worker in enumerate(students, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                idx,
                worker.get('name', ''),
                worker.get('number', ''),
                worker.get('z', 0)
            )
        )

    print_line()


def print_select():
    cn = 0
    for student in students:
        if "2" in student.get('z', ''):
            cn -= 1
            print(
                '{:>4} {}'.format('*', student.get('name', '')),
                '{:>1} {}'.format('группа №', student.get('number', ''))
            )
    if cn == 0:
        print('Таких студентов нет')
