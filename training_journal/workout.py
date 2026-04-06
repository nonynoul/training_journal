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

def short_workout_info(workout):
    """
    Краткая информация о тренировке
    :param workout: Объект Workout
    :return: Строка с датой и количеством упражнений
    """
    return f'{workout.date}: {len(workout.exercises)} упражнений, {workout.total_duration()} мин'
