from .exercise import Exercise, CardioExercise
from .log import WorkoutLog
from .workout import Workout, short_workout_info

def input_number(text):
    """
    Безопасный ввод целого числа.
    :param text: Текст запроса
    :return: Введённое число
    """
    while True:
        value = input(text).strip()
        try:
            return int(value)
        except ValueError:
            print('Нужно ввести целое число')

def create_regular_exercise():
    """
    Создаёт обычное упражнение через ввод пользователя
    """
    name = input('Введите название упражнения: ').strip()
    exercise_type = input('Введите тип упражнения: ').strip()
    duration = input_number('Введите длительность в минутах: ')
    return Exercise(name, exercise_type, duration)

def create_cardio_exercise():
    """
    Создаёт кардио-упражнение через ввод пользователя
    """
    name = input('Введите название кардио: ').strip()
    duration = input_number('Введите длительность в минутах: ')
    intensity = input('Введите интенсивность: ').strip()
    return CardioExercise(name, duration, intensity)

def create_workout():
    """
    Создаёт тренировку через ввод пользователя
    """
    date = input('Введите дату тренировки (YYYY-MM-DD): ').strip()
    workout = Workout(date)

    while True:
        print('\n1 - добавить обычное упражнение')
        print('2 - добавить кардио')
        print('0 - закончить тренировку')

        choice = input('Ваш выбор: ').strip()

        if choice == '1':
            ex = create_regular_exercise()
            workout.add_exercise(ex)
            print('Упражнение добавлено')
        elif choice == '2':
            ex = create_cardio_exercise()
            workout.add_exercise(ex)
            print('Кардио добавлено')
        elif choice == '0':
            break
        else:
            print('Нет такого пункта')
    return workout

def show_all_workouts(log):
    """
    Показывает все тренировки из журнала
    """
    if len(log.workouts) == 0:
        print('Тренировок пока нет')
        return

    print()
    for i, workout in enumerate(log.workouts, 1):
        print(f'{i}. {short_workout_info(workout)}')
        for ex in workout.exercises:
            print(f'{ex}')

def main():
    """
    Главная функция программы
    """
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

if __name__ == '__main__':
    main()
