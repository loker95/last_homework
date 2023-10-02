class Person:
    def init(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def introduce(self):
        pass

class Employee(Person):
    def init(self, name, age, position):
        super().init(name, age)
        self.__position = position

    def get_position(self):
        return self.__position

    def introduce(self):
        print(f"Привет, меня зовут {self.get_name()} и мне "
              f"{self.get_age()} лет. Я работаю на позиции {self.get_position()}.")


class Student(Person):
    def init(self, name, age, grade):
        super().init(name, age)
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def introduce(self):
        print(f"Привет, меня зовут {self.get_name()} и мне {self.get_age()} лет. Я студент {self.get_grade()} курса.")


class Department:
    def init(self, name):
        self.__name = name
        self.__employees = []
        self.__students = []

    def get_name(self):
        return self.__name

    def add_employee(self, employee):
        self.__employees.append(employee)

    def add_student(self, student):
        self.__students.append(student)

    def list_people(self):
        print(f"Отдел {self.get_name()}:")
        for employee in self.__employees:
            employee.introduce()
        for student in self.__students:
            student.introduce()


class Academy:
    def init(self, name):
        self.__name = name
        self.__departments = []

    def get_name(self):
        return self.__name

    def add_department(self, department):
        self.__departments.append(department)

    def list_people(self):
        print(f"Академия {self.get_name()}:")
        for department in self.__departments:
            department.list_people()


math_teacher = Employee("Иван Иванов", 40, "Преподаватель математики")
history_teacher = Employee("Мария Петрова", 35, "Преподаватель истории")
student1 = Student("Анна Смирнова", 20, 2)
student2 = Student("Петр Иванов", 22, 3)
math_department = Department("Отдел математики")
history_department = Department("Отдел истории")
academy = Academy("Лучшая академия")

math_department.add_employee(math_teacher)
history_department.add_employee(history_teacher)
math_department.add_student(student1)
history_department.add_student(student2)
academy.add_department(math_department)
academy.add_department(history_department)

academy.list_people()
