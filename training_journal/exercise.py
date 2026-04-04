class Exercise:
    """
    Класс обычного упражнения
    """

    def __init__(self, name, exercise_type, duration):
        """
        Конструктор упражнения
        :param name: Название упражнения
        :param exercise_type: Тип упражнения
        :param duration: Длительность в минутах
        """
        self.name = name
        self.exercise_type = exercise_type
        self.duration = duration

    def __str__(self):
        """
        Наименование упражнения
        :return: Полное название упражнения
        """
        return f'{self.name} | тип: {self.exercise_type} | {self.duration} мин'


class CardioExercise(Exercise):
    """
    Класс кардио-упражнения
    """

    def __init__(self, name, duration, intensity):
        """
        Конструктор кардио-упражнения
        :param name: Название упражнения
        :param duration: Длительность в минутах
        :param intensity: Интенсивность
        """
        super().__init__(name, 'кардио', duration)
        self.intensity = intensity

    def __str__(self):
        """
        Наименование упражнения
        :return: Полное название упражнения
        """
        return f'{self.name} | кардио | {self.duration} мин | интенсивность: {self.intensity}'
