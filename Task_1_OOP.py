class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за домашние задания: {self.average_S_grades():.1f}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def average_S_grades(self):
        all_grades = []
        for s_grade in self.grades.values():
            all_grades.extend(s_grade)
        if all_grades:
            amount = sum(all_grades) / len(all_grades)
        else:
            amount = 0
        return amount

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            return NotImplemented
        return self.average_S_grades() < other_student.average_S_grades()

    def __gt__(self, other_student):
        if not isinstance(other_student, Student):
            return NotImplemented
        return self.average_S_grades() > other_student.average_S_grades()

    def __eq__(self, other_student):
        if not isinstance(other_student, Student):
            return NotImplemented
        return self.average_S_grades() == other_student.average_S_grades()

    def __ne__(self, other_student):
        if not isinstance(other_student, Student):
            return NotImplemented
        return self.average_S_grades() != other_student.average_S_grades()

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка'
        if course not in lecturer.courses_attached  or course not in self.courses_in_progress:
            return 'Ошибка'
        if not isinstance(grade, int) or not 1 <= grade <= 10:
            return 'Ошибка: оценка должна быть от 1 до 10'
        if course in lecturer.grades:
            lecturer.grades[course] += [grade]
        else:
            lecturer.grades[course] = [grade]


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached =[]


class Lecturer(Mentor):
    def __init__(self, name, surname):
       super().__init__(name, surname)
       self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за лекции: {self.average_L_grades():.1f}')

    def average_L_grades(self):
        all_grades = []
        for l_grade in self.grades.values():
            all_grades.extend(l_grade)
        if all_grades:
            amount = sum(all_grades) / len(all_grades)
        else:
            amount = 0
        return amount

    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            return NotImplemented
        return self.average_L_grades() < other_lecturer.average_L_grades()

    def __gt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            return NotImplemented
        return self.average_L_grades() > other_lecturer.average_L_grades()

    def __eq__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            return NotImplemented
        return self.average_L_grades() == other_lecturer.average_L_grades()

    def __ne__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            return NotImplemented
        return self.average_L_grades() != other_lecturer.average_L_grades()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname}')

    def rate_hw(self, student, course, grade):
        if not isinstance(student, Student):
            return 'Ошибка'
        if course not in self.courses_attached or course not in student.courses_in_progress:
            return 'Ошибка'
        if not isinstance(grade, int) or not 1 <= grade <= 10:
            return 'Ошибка: оценка должна быть от 1 до 10'
        if course in student.grades:
            student.grades[course].append(grade)
        else:
            student.grades[course] = [grade]


def average_students_grades(students_list, course):
    all_grades = []
    for student in students_list:
        if course in student.grades:
            all_grades.extend(student.grades[course])
    if all_grades:
        return f'{sum(all_grades) / len(all_grades):.1f}'
    else:
        return 0


def average_lecturers_grades(lecturers_list, course):
    all_grades = []
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    if all_grades:
        return f'{sum(all_grades) / len(all_grades):.1f}'
    else:
        return 0


#Проверка работоспособности
# Создание объектов
student_1 = Student('Анна', 'Смирнова', 'Ж')
student_2 = Student('Кирилл', 'Рыков', 'М')
reviewer_1 = Reviewer('Дмитрий', 'Козлов')
reviewer_2 = Reviewer('Ольга', 'Котова')
lecturer_1 = Lecturer('Елена', 'Волкова')
lecturer_2 = Lecturer('Андрей', 'Марков')

# Настройка курсов
student_1.courses_in_progress = ['Python', 'JavaScript']
student_2.courses_in_progress = ['Python', 'C++']
student_1.finished_courses = ['Основы программирования']
student_2.finished_courses = ['Основы программирования']
reviewer_1.courses_attached = ['Python', 'JavaScript']
reviewer_2.courses_attached = ['C++']
lecturer_1.courses_attached = ['Python', 'C++']
lecturer_2.courses_attached = ['JavaScript']

# Выставление оценок за ДЗ (ревьюер студенту)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'JavaScript', 7)
reviewer_1.rate_hw(student_1, 'JavaScript', 8)
reviewer_1.rate_hw(student_1, 'JavaScript', 8)
reviewer_1.rate_hw(student_2, 'Python', 6)
reviewer_1.rate_hw(student_2, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_2, 'C++', 8)
reviewer_2.rate_hw(student_2, 'C++', 9)
reviewer_2.rate_hw(student_2, 'C++', 8)

# Оценка лекций (студент лектору)
student_1.rate_lecture(lecturer_1, 'Python', 8)
student_1.rate_lecture(lecturer_2, 'JavaScript', 8)
student_2.rate_lecture(lecturer_1, 'Python', 10)
student_2.rate_lecture(lecturer_1, 'C++', 8)

# Создаем списки всех студентов и лекторов
all_students = [student_1, student_2]
all_lecturers = [lecturer_1, lecturer_2]

# Вывод информации
print('ПРОВЕРКА РАБОТОСПОСОБНОСТИ')
print('=' * 60, end='\n\n')
print('Студенты')
print('=' * 60, end='\n\n')
print(student_1, end='\n\n')
print(student_2, end='\n\n')
print('Сравнение успеваемости студентов')
print('=' * 60, end='\n\n')
print(f'Студент {student_2.name} учится лучше, чем студент {student_1.name}: {student_2 > student_1}') #False
print(f'Студент {student_2.name} учится лучше, чем студент {student_1.name}: {student_2 < student_1}') #True
print(f'Студент {student_1.name} учится так же как и {student_2.name}: {student_2 == student_1}',) #False
print(f'Студенты {student_2.name} и {student_1.name} учатся неодинаково: {student_2 != student_1}', end='\n\n') #True
print('Лекторы')
print('=' * 60, end='\n\n')
print(lecturer_1, end='\n\n')
print(lecturer_2, end='\n\n')
print('Сравнение лекторов')
print('=' * 60, end='\n\n')
print(f'Лектор {lecturer_1.name} по мнению учеников лучше преподает, чем {lecturer_2.name}: {lecturer_1 > lecturer_2}') #True
print(f'Лектор {lecturer_1.name} по мнению учеников хуже преподает, чем {lecturer_2.name}: {lecturer_1 < lecturer_2}') #False
print(f'По мнению учеников лекторы {lecturer_2.name} и {lecturer_1.name} преподают одинаково: {lecturer_2 == lecturer_1}') #False
print(f'По мнению учеников лекторы {lecturer_2.name} и {lecturer_1.name} преподают неодинаково: {lecturer_1 != lecturer_2}', end='\n\n') #True
print('Ревьюеры')
print('=' * 60, end='\n\n')
print(reviewer_1, end='\n\n')
print(reviewer_2, end='\n\n')
print('Средние оценки студентов за домашние задания по курсам')
print('=' * 60, end='\n\n')
print(f'По курсу Python: {average_students_grades(all_students, "Python")}')
print(f'По курсу JavaScript: {average_students_grades(all_students, "JavaScript")}')
print(f'По курсу C++: {average_students_grades(all_students, "C++")}', end='\n\n')
print('Средние оценки лекторов за лекции по курсам')
print('=' * 60, end='\n\n')
print(f'По курсу Python: {average_lecturers_grades(all_lecturers, "Python")}')
print(f'По курсу JavaScript: {average_lecturers_grades(all_lecturers, "JavaScript")}')
print(f'По курсу C++: {average_lecturers_grades(all_lecturers, "C++")}')