import random


def answer():
    i = 24
    grade = []

    for i in range(0, i):
        grade.append(random.randint(2, 5))

    print(f"Массив оценок: {grade}")

    count = 0
    for i in grade:
        count += grade[i] / 5;

    print(f"Из них пятёрок: {count:0.1f}")