#!/usr/bin/env python3

# Главный скрипт запуска программы учёта тренировок

from training_journal.workout import Workout
from training_journal.log import WorkoutLog

def input_number(text):
    """
    Безопасный ввод целого числа
    :param text: Текст запроса
    :return: Введённое число
    """
    while True:
        value = input(text).strip()
        try:
            return int(value)
        except ValueError:
            print('Нужно ввести целое число')

def show_all_workouts(log):
    """
    Показывает все тренировки из журнала
    :param log: Объект WorkoutLog
    """
    if len(log.workouts) == 0:
        print('Тренировок пока нет')
        return
    
    print()
    for i, workout in enumerate(log.workouts, 1):
        print(f'{i}. {short_workout_info(workout)}')
        for ex in workout.exercises:
            print(f'   {ex}')

def short_workout_info(workout):
    """
    Краткая информация о тренировке
    :param workout: Объект Workout
    :return: Строка с датой и количеством упражнений
    """
    return f'{workout.date}: {len(workout.exercises)} упражнений, {workout.total_duration()} мин'



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
            workout = Workout.create_workout()
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
