# Модуль с классами упражнений
# Содержит классы Exercise и CardioExercise

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

    def __str__(self):
        """
        Наименование упражнения
        :return: Полное название упражнения
        """
        return f'{self.name} | тип: {self.exercise_type} | {self.duration} мин'

    @staticmethod
    def create_regular_exercise():
        """
        Создаёт обычное упражнение через ввод пользователя
        """
        name = input('Введите название упражнения: ').strip()
        exercise_type = input('Введите тип упражнения: ').strip()
        duration = input_number('Введите длительность в минутах: ')
        return Exercise(name, exercise_type, duration)

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

    @staticmethod
    def create_cardio_exercise():
        """
        Создаёт кардио-упражнение через ввод пользователя
        """
        name = input('Введите название кардио: ').strip()
        duration = input_number('Введите длительность в минутах: ')
        intensity = input('Введите интенсивность: ').strip()
        return CardioExercise(name, duration, intensity)

if __name__ == '__main__':
    ...
    
