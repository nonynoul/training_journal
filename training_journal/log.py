class WorkoutLog:
    """
    Журнал тренировок
    """

    def __init__(self):
        """
        Конструктор журнала
        """
        self.workouts = []

    def add_workout(self, workout):
        """
        Добавляет тренировку в журнал
        :param workout: Объект Workout
        """
        self.workouts.append(workout)

    def count(self):
        """
        Возвращает количество тренировок
        """
        return len(self.workouts)

    def total_duration(self):
        """
        Подсчитывает общее время всех тренировок
        """
        total = 0
        for workout in self.workouts:
            total += workout.total_duration()
        return total

    def minutes_to_text(self, minutes):
        """
        Переводит минуты в читаемый формат
        :param minutes: Количество минут
        :return: Строка вида 'X ч Y мин'
        """
        if minutes == 0:
            return '0 мин'

        hours = minutes // 60
        mins = minutes % 60

        if hours == 0:
            return f'{mins} мин'
        if mins == 0:
            return f'{hours} ч'
        return f'{hours} ч {mins} мин'

    def get_statistics(self):
        """
        Собирает статистику по типам упражнений.
        :return: Словарь {тип_упражнения: общее_время}
        """
        stats = {}
        for workout in self.workouts:
            for ex in workout.exercises:
                ex_type = ex.exercise_type
                if ex_type in stats:
                    stats[ex_type] += ex.duration
                else:
                    stats[ex_type] = ex.duration
        return stats

    def statistics_text(self):
        """
        Возвращает текст со статистикой тренировок
        :return: Строка со статистикой
        """
        stats = self.get_statistics()
        lines = []
        lines.append(f'Количество тренировок: {self.count()}')
        lines.append(f'Общая длительность: {self.minutes_to_text(self.total_duration())}')
        lines.append('Статистика по типам упражнений: ')
        if len(stats) == 0:
            lines.append('Нет данных')
        else:
            for ex_type, duration in stats.items():
                lines.append(f' - {ex_type}: {duration} мин')

        return ' \n'.join(lines)

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
