class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Student(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_in_progress = []
        self.grades = {}

    def add_course(self, course_name):
        self.courses_in_progress.append(course_name)

    def rate_lecturer(self, lecturer, course_name, grade):
        if course_name in self.courses_in_progress and isinstance(lecturer, Lecturer):
            if course_name in lecturer.grades:
                lecturer.grades[course_name].append(grade)
            else:
                lecturer.grades[course_name] = [grade]
        else:
            print(f"Ошибка: Лектор не ведет курс {course_name} или студент не записан на этот курс.")


class Reviewer(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses = []

    def add_course(self, course_name):
        self.courses.append(course_name)

    def rate_student(self, student, course_name, grade):
        if course_name in self.courses and isinstance(student, Student):
            if course_name in student.grades:
                student.grades[course_name].append(grade)
            else:
                student.grades[course_name] = [grade]
        else:
            print(f"Ошибка: Студент не записан на курс {course_name} или рецензент не ведет этот курс.")


class Lecturer(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"{self.name} {self.surname}"


student1 = Student("Иван", "Иванов")
student1.add_course("Математика")
student1.add_course("Физика")
lecturer1 = Lecturer("Петр", "Петров")
lecturer2 = Lecturer("Сергей", "Сергеев")
# Студент выставляет оценку лектору
student1.rate_lecturer(lecturer1, "Математика", 8)
student1.rate_lecturer(lecturer1, "Математика", 9)

print(f"Оценки лектора {lecturer1}: {lecturer1.grades}")
# Рецензент выставляет оценку студенту
reviewer = Reviewer("Алексей", "Алексеев")
reviewer.add_course("Математика")
reviewer.rate_student(student1, "Математика", 10)

print(f"Оценки студента {student1.name} {student1.surname}: {student1.grades}")
