#!/usr/bin/env python3

from .exercise import Exercise, CardioExercise
from .log import WorkoutLog
from .workout import Workout, short_workout_info

if __name__ == '__main__':
    log = WorkoutLog()

    while True:
        print('\nУчёт тренировок')
        print('1 - добавить тренировку')
        print('2 - показать тренировки')
        print('3 - показать статистику')
        print('0 - выход')

        choice = input('Ваш выбор: ').strip()

        if choice == '1':
            workout = create_workout()
            log.add_workout(workout)
            print('Тренировка сохранена в журнале')
        elif choice == '2':
            show_all_workouts(log)
        elif choice == '3':
            print(log.statistics_text())
        elif choice == '0':
            print('Выход из программы')
            break
        else:
            print('Нет такого пункта')
