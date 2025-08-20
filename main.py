class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # Список прикрепленных курсов

# Дочерний класс Lector (лектор)
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Словарь с оценками, ключ - название курса, значение - список оценок

# Дочерний класс Reviewer (ревьювер/преподаватель, проверяющий домашнюю работу)
class Reviewer(Mentor):
    pass

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')

print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer.courses_attached)    # []
print(reviewer.courses_attached)    # []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lecture(self, lecturer, course_name, grade):
        if isinstance(lecturer,
                      Lecturer) and course_name in lecturer.courses_attached and course_name in self.courses_in_progress:
            if course_name not in lecturer.grades:
                lecturer.grades[course_name] = []
            lecturer.grades[course_name].append(grade)
        else:
            return f'Ошибка'

class Reviewer(Mentor):
    def rate_hw(self, student, course_name, grade):
        if course_name in self.courses_attached and course_name in student.courses_in_progress:
            if course_name not in student.grades:
                student.grades[course_name] = []
            student.grades[course_name].append(grade)
        else:
            return f'Ошибка'

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))   # None
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
print(student.rate_lecture(lecturer, 'C++', 8))      # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка

print(lecturer.grades)  # {'Python': [7]}

from statistics import mean

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\\nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        """Вычисляет средний балл лектора"""
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        return round(mean(all_grades), 1) if all_grades else 0

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __str__(self):
        avg_grade = self.average_grade()
        return f'{super().__str__()}\\nСредняя оценка за лекции: {avg_grade}'

class Reviewer(Mentor):
    def rate_hw(self, student, course_name, grade):
        if course_name in self.courses_attached and course_name in student.courses_in_progress:
            if course_name not in student.grades:
                student.grades[course_name] = []
            student.grades[course_name].append(grade)
        else:
            return f'Ошибка'

    def __str__(self):
        return f'{super().__str__()}'

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}



    def add_course(self, course_name):
        self.courses_in_progress.append(course_name)

    def finish_course(self, course_name):
        self.finished_courses.append(course_name)
        self.courses_in_progress.remove(course_name)

    def rate_lecture(self, lecturer, course_name, grade):
        if isinstance(lecturer, Lecturer) and course_name in lecturer.courses_attached and course_name in self.courses_in_progress:
            if course_name not in lecturer.grades:
                lecturer.grades[course_name] = []
            lecturer.grades[course_name].append(grade)
        else:
            return f'Ошибка'

    def average_grade(self):
        """Вычисляем общий средний балл по всем курсам"""
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        return round(mean(all_grades), 1) if all_grades else 0

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __str__(self):
        avg_grade = self.average_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return (
            f'Имя: {self.name}\\n'
            f'Фамилия: {self.surname}\\n'
            f'Средняя оценка за домашние задания: {avg_grade}\\n'
            f'Курсы в процессе изучения: {courses_in_progress_str}\\n'
            f'Завершенные курсы: {finished_courses_str}'
        )

# Тестируем реализацию:
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Алексей', 'Александров')
reviewer = Reviewer('Петр', 'Петров')
student1 = Student('Роев', 'Егор', 'Мужской')
student2 = Student('Олехина', 'Анна', 'Женский')

student1.add_course('Python')
student2.add_course('Python')
lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Python']
reviewer.courses_attached += ['Python']

# Добавление оценок лекторам и рецензенту
student1.rate_lecture(lecturer1, 'Python', 9)
student2.rate_lecture(lecturer1, 'Python', 8)
student1.rate_lecture(lecturer2, 'Python', 7)
student2.rate_lecture(lecturer2, 'Python', 6)

# Оценивание домашней работы от Reviewer
reviewer.rate_hw(student1, 'Python', 8)
reviewer.rate_hw(student2, 'Python', 9)

# Выводим информацию о студентах и преподавателях
print(lecturer1)  # Среднее значение за лекции
print(lecturer2)  # Среднее значение за лекции
print(student1)   # Информация о студенте + средняя оценка
print(student2)   # Информация о студенте + средняя оценка

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Метод для вычисления средней оценки студента
    def average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0

    # Важный метод для выставления оценок лекторам
    def rate_lecture(self, lecturer, course_name, grade):
        if isinstance(lecturer, Lecturer) and course_name in lecturer.courses_attached and course_name in self.courses_in_progress:
            if course_name not in lecturer.grades:
                lecturer.grades[course_name] = []
            lecturer.grades[course_name].append(grade)
        else:
            return f'Ошибка'

    # Метод для красивого вывода информации о студенте
    def __str__(self):
        avg_grade = self.average_grade()
        return f'Имя: {self.name}\\nФамилия: {self.surname}\\nСредняя оценка за домашние задания: {avg_grade}\\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    # Операции сравнения
    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()


# Другие классы и методы остались прежними

# Создаем экземпляры классов
mentor1 = Mentor('Виктор', 'Сергеевич')
mentor2 = Mentor('Анна', 'Николаевна')

lecturer1 = Lecturer('Максим', 'Корнеев')
lecturer2 = Lecturer('Дарья', 'Шарова')

reviewer1 = Reviewer('Роман', 'Чернецов')
reviewer2 = Reviewer('Наталья', 'Дроздова')

student1 = Student('Егор', 'Роев', 'Мужской')
student2 = Student('Анна', 'Олехина', 'Женский')

# Настройка курсов для студентов
student1.courses_in_progress.extend(['Python', 'JavaScript'])
student2.courses_in_progress.extend(['Python', 'C++'])

# Назначим курсы лекторам
lecturer1.courses_attached.extend(['Python', 'JavaScript'])
lecturer2.courses_attached.extend(['Python', 'C++'])

# Назначим курсы ревизерам
reviewer1.courses_attached.extend(['Python', 'JavaScript'])
reviewer2.courses_attached.extend(['Python', 'C++'])

# Поставим оценки за лекции
student1.rate_lecture(lecturer1, 'Python', 9)
student2.rate_lecture(lecturer1, 'Python', 8)
student1.rate_lecture(lecturer2, 'Python', 7)
student2.rate_lecture(lecturer2, 'Python', 6)

# Постановка оценок за домашнюю работу
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student1, 'JavaScript', 9)
reviewer2.rate_hw(student2, 'C++', 8)

from statistics import mean

# Функция для подсчета средней оценки за лекции среди лекторов
def average_lecture_grade(lecturers, course_name):
    grades = []
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            grades.extend(lecturer.grades[course_name])
    return round(mean(grades), 1) if grades else 0

# Функция для подсчета средней оценки за домашние задания среди студентов
def average_homework_grade(students, course_name):
    grades = []
    for student in students:
        if course_name in student.grades:
            grades.extend(student.grades[course_name])
    return round(mean(grades), 1) if grades else 0

# Подготовим список студентов и лекторов
lecturers = [lecturer1, lecturer2]
students = [student1, student2]

# Посчитаем среднюю оценку за лекции по курсу "Python"
avg_lecture_grade = average_lecture_grade(lecturers, 'Python')
print(f"Средняя оценка за лекции по курсу 'Python': {avg_lecture_grade}")

# Посчитаем среднюю оценку за домашние задания по курсу "Python"
avg_homework_grade = average_homework_grade(students, 'Python')
print(f"Средняя оценка за домашние задания по курсу 'Python': {avg_homework_grade}")

# Выводим информацию о студентах и преподавателях
print("\\nИнформация о студентах и преподавателях:")
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
