class Workout:
    """
    Класс тренировки
    """

    def __init__(self, date):
        """
        Конструктор тренировки
        :param date: Дата тренировки (ГГГГ-ММ-ДД)
        """
        self.date = date
        self.exercises = []

    def add_exercise(self, exercise):
        """
        Добавляет упражнение в тренировку.
        :param exercise: Объект Exercise или CardioExercise
        """
        self.exercises.append(exercise)

    def total_duration(self):
        """
        Подсчитывает общую длительность тренировки
        :return: Суммарное время всех упражнений
        """
        total = 0
        for ex in self.exercises:
            total += ex.duration
        return total

    def __str__(self):
        """
        Строковое представление тренировки
        :return: Полное название тренировки
        """
        return f'{self.date}: {len(self.exercises)} упражнений, всего {self.total_duration()} мин'


def short_workout_info(workout):
    """
    Краткая информация о тренировке
    :param workout: Объект Workout
    :return: Строка с датой и количеством упражнений
    """
    return f'{workout.date}: {len(workout.exercises)} упражнений, {workout.total_duration()} мин'
