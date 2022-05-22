class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: " \
               f"{round(self.av_rating(self.grades), 2)}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Для сравнения выбран не студент!')
            return
        else:
            if self.av_rating(self.grades) > other.av_rating(other.grades):
                print(f'Средний балл {self.name} {self.surname} выше, чем у {other.name} {other.surname}')
                return
            else:
                print(f'Средний балл {other.name} {other.surname} выше, чем у {self.name} {self.surname}')
                return

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course \
                in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def av_rating(self, grades):
        new_grades = []
        for grade in grades.values():
            new_grades += grade
        average_ = sum(new_grades)/len(new_grades)
        return average_


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.av_rating(self.grades), 2)}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Для сравнения выбран не лектор!')
            return
        else:
            if self.av_rating(self.grades) > other.av_rating(other.grades):
                print(f'Средний балл {self.name} {self.surname} выше, чем у {other.name} {other.surname}')
                return
            else:
                print(f'Средний балл {other.name} {other.surname} выше, чем у {self.name} {self.surname}')
                return

    def av_rating(self, grades):
        new_grades = []
        for grade in grades.values():
            new_grades += grade
        average_ = sum(new_grades)/len(new_grades)
        return average_


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Создаём по 2 экземпляра каждого класса
best_student = Student('Best', 'Student', 'Male')
some_student = Student('Some', 'Student_', 'Female')

best_mentor = Mentor('Best', 'Mentor')
some_mentor = Mentor('Some', 'Student_')

best_lecturer = Lecturer('Best', 'Lecturer')
some_lecturer = Lecturer('Some', 'Lecturer_')

best_reviewer = Reviewer('Best', 'Reviewer')
some_reviewer = Reviewer('Some', 'Reviewer_')

# Добавляем студентам, ревьюерам и лекторам курсы
best_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Git']
some_student.finished_courses += ['Git']

best_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Python']

best_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Python']

# Ставим 2м студентам оценки за курс по Python
some_reviewer.rate_student(best_student, 'Python', 9)
some_reviewer.rate_student(best_student, 'Python', 9)
some_reviewer.rate_student(best_student, 'Python', 9)

some_reviewer.rate_student(some_student, 'Python', 5)
some_reviewer.rate_student(some_student, 'Python', 7)
some_reviewer.rate_student(some_student, 'Python', 7)

# Ставим 2м лекторам оценки за курс по Python
best_student.rate_lecturer(best_lecturer, 'Python', 10)
best_student.rate_lecturer(best_lecturer, 'Python', 10)
best_student.rate_lecturer(best_lecturer, 'Python', 10)

best_student.rate_lecturer(some_lecturer, 'Python', 8)
best_student.rate_lecturer(some_lecturer, 'Python', 8)
best_student.rate_lecturer(some_lecturer, 'Python', 8)

# Вызываем перезаписанный магический метод __lt__
best_student.__lt__(some_student)
some_lecturer.__lt__(best_lecturer)
print('---------------')
print(best_student)
print(some_student)
print('---------------')
print(best_lecturer)
print(some_lecturer)
print('---------------')
print(best_reviewer)
print(some_reviewer)


# Добавляем студентам курсов и оценок
best_student.courses_in_progress += ['Java']
best_student.courses_in_progress += ['C++']
best_reviewer.courses_attached += ['Java']
best_reviewer.courses_attached += ['C++']
best_reviewer.rate_student(best_student, 'Java', 8)
best_reviewer.rate_student(best_student, 'Java', 8)
best_reviewer.rate_student(best_student, 'Java', 10)
best_reviewer.rate_student(best_student, 'C++', 6)
best_reviewer.rate_student(best_student, 'C++', 5)
best_reviewer.rate_student(best_student, 'C++', 4)
print('---------------')
print(best_student.grades)

some_student.courses_in_progress += ['Java']
some_student.courses_in_progress += ['C++']
best_reviewer.courses_attached += ['Java']
best_reviewer.courses_attached += ['C++']
best_reviewer.rate_student(some_student, 'Java', 10)
best_reviewer.rate_student(some_student, 'Java', 6)
best_reviewer.rate_student(some_student, 'Java', 6)
best_reviewer.rate_student(some_student, 'C++', 10)
best_reviewer.rate_student(some_student, 'C++', 9)
best_reviewer.rate_student(some_student, 'C++', 9)
print('---------------')
print(some_student.grades)

# Добавляем лекторам курсов и оценок
best_lecturer.courses_attached += ['Java']
best_lecturer.courses_attached += ['C++']
best_student.rate_lecturer(best_lecturer, 'Java', 10)
best_student.rate_lecturer(best_lecturer, 'Java', 10)
best_student.rate_lecturer(best_lecturer, 'Java', 9)
best_student.rate_lecturer(best_lecturer, 'C++', 9)
best_student.rate_lecturer(best_lecturer, 'C++', 10)
best_student.rate_lecturer(best_lecturer, 'C++', 9)
print('---------------')
print(best_lecturer.grades)

some_lecturer.courses_attached += ['Java']
some_lecturer.courses_attached += ['C++']
some_student.rate_lecturer(some_lecturer, 'Java', 9)
best_student.rate_lecturer(some_lecturer, 'Java', 8)
some_student.rate_lecturer(some_lecturer, 'Java', 9)
best_student.rate_lecturer(some_lecturer, 'C++', 8)
some_student.rate_lecturer(some_lecturer, 'C++', 10)
best_student.rate_lecturer(some_lecturer, 'C++', 9)
print('---------------')
print(some_lecturer.grades)
print('---------------')


# функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса 
def all_students_avg_grade(students_list, course_name):
    all_grades = []
    for student in students_list:
        for key, value in student.grades.items():
            if key == course_name:
                all_grades += value
            else:
                pass
    avg_grade = sum(all_grades)/len(all_grades)
    return f'Средние оценки студентов за лекции по {course_name} - {round(avg_grade, 2)}'

any_students = [best_student, some_student]
print(all_students_avg_grade(any_students, 'Java'))


# функция для подсчета средней оценки за домашние задания по всем преподавателям в рамках конкретного курса 
def all_lecturers_avg_grade(lecturers_list, course_name):
    all_grades = []
    for lecturer in lecturers_list:
        for key, value in lecturer.grades.items():
            if key == course_name:
                all_grades += value
            else:
                pass
    avg_grade = sum(all_grades)/len(all_grades)
    return f'Средние оценки преподавателей за лекции по {course_name} - {round(avg_grade, 2)}'


any_lecturers = [best_lecturer, some_lecturer]
print(all_lecturers_avg_grade(any_lecturers, 'Python'))