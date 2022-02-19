#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import student as st

list_commands = (
        {'name': 'help', 'fun': st.print_list, 'desc': 'добавить студента'},
        {'name': 'add', 'fun': st.add, 'desc': 'вывести список студентов'},
        {'name': 'select', 'fun': st.print_select, 'desc': 'вывести список студентов, имеющих оценку 2'},
        {'name': 'list', 'fun': st.print_list, 'desc': 'отобразить справку'}
)


def get():
    return input(">>> ").lower()


def is_name(is_name_command):
    for command in list_commands:
        if is_name_command == command['name']:
            return True

    return False


def call(in_name_command):
    for command in list_commands:
        if in_name_command == command['name']:
            return command['fun']()

    return False
