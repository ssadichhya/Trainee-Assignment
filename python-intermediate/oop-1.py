class University:
    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__departments = []

    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__location

    def get_departments(self):
        return self.__departments

    def add_department(self, department):
        self.__departments.append(department)

    def display_details(self):
        print(f"University: {self.__name}")
        print(f"Location: {self.__location}")
        print("Departments:")
        for department in self.__departments:
            print(f" - {department}")


class Department(University):
    def __init__(self, name, location, department_name, head_of_department):
        super().__init__(name, location)
        self.__department_name = department_name
        self.__head_of_department = head_of_department
        self.__courses_offered = []


    def add_course(self, course):
        self.__courses_offered.append(course)

    def display_details(self):
        super().display_details()
        print(f"Department: {self.__department_name}")
        print(f"Head of Department: {self.__head_of_department}")
        print("Courses Offered:")
        for course in self.__courses_offered:
            print(f" - {course}")


university = University("Tribhuwan university", "Balkhu")

department1 = Department(
    "Tribhuwan University", "Balkhu", "Computer Science", "prateek")
department2 = Department(
    "kathmandu University", "dhulikhel", "Mathematics", "upama")

department1.add_course("Introduction to Programming")
department1.add_course("Data Structures")
department2.add_course("Calculus")
department2.add_course("Linear Algebra")

university.add_department(department1)
university.add_department(department2)

university.display_details()

print("\nDepartment Details:")
for department in university.get_departments():
    department.display_details()
    print()
