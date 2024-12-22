import math
import numpy as np
import curses





class Person:
    def __init__(self, student_id, name, dob):
        self._student_id = student_id
        self._name = name
        self._dob = dob

    def get_id(self):
        return self._student_id

    def get_name(self):
        return self._name

    def get_dob(self):
        return self._dob

    def __str__(self):
        return f"ID: {self._student_id}, Name: {self._name}, DoB: {self._dob}"


class Course:
    def __init__(self, course_id, name, credits):
        self._course_id = course_id
        self._name = name
        self._credits = credits

    def get_id(self):
        return self._course_id

    def get_name(self):
        return self._name
    
    def get_credits(self):
        return self._credits

    def __str__(self):
        return f"ID: {self._course_id}, Name: {self._name}, credits: {self._credits}"


class StudentMarkManagement:
    def __init__(self):
        self._students = []
        self._courses = []
        self._marks = {}
        self._gpa = {}

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
            self._students.append(Person(student_id, name, dob))

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            credits = int(input("ENter course credits: "))
            self._courses.append(Course(course_id, name, credits))

    def list_courses(self):
        print("\nList of courses:")
        for course in self._courses:
            print(course)

    def list_students(self):
        print("\nList of students:")
        for student in self._students:
            print(student)

    def select_course(self):
        print("\nAvailable courses:")
        for idx, course in enumerate(self._courses, 1):
            print(f"{idx}. {course.get_name()} (ID: {course.get_id()})")
        selected_index = int(input("Select a course by number: ")) - 1
        return self._courses[selected_index]

    def input_marks(self, course):
        print(f"\nEntering marks for course: {course.get_name()} (ID: {course.get_id()})")
        for student in self._students:
            mark = float(input(f"Enter marks for {student.get_name()} (ID: {student.get_id()}): "))
            true_mark = math.floor(mark * 10) / 10
            self._marks[(student.get_id(), course.get_id())] = true_mark

    def calculate_gpa(self):
        for student in self._students:
            total_credits = 0
            weight_sum = 0
            for course in self._courses:
                key = (student.get_id(), course.get_id())
                mark = self._marks.get(key, None)
                if mark is not None:
                    credits = course.get_credits()
                    total_credits += credits
                    weight_sum += mark * credits
            gpa = weight_sum / total_credits if total_credits > 0 else 0
            self._gpa[student.get_id()] = round(gpa, 2)

    def sort_student_by_gpa(self):
        self.calculate_gpa()
        sorted_students = sorted(self._students, key = lambda s: self._gpa.get(s.get_id(), 0), reverse = True)
        print("\n Students sorted by GPA: ")
        for students in sorted_students:
            print(f"{students.get_name()}, ID: {students.get_id()}, gpa: {self._gpa.get(students.get_id(), 0)}")





    def show_student_marks(self, course):
        print(f"\nMarks for course: {course.get_name()} (ID: {course.get_id()})")
        for student in self._students:
            key = (student.get_id(), course.get_id())
            mark = self._marks.get(key, "no mark  ")
            print(f"{student.get_name()} (ID: {student.get_id()}): {mark}")

    def decorated_ui(self, stdscr):
        curses.curs_set(0)
        stdscr.clear()
        stdscr.addstr(0, 0, "student mm system", curses.A_COLOR)
        stdscr.addstr(2, 0, "Press a key")
        stdscr.refresh()
        stdscr.getch()
        self.run()
    



    def run(self):
        self.input_students()
        self.input_courses()

        while True:
            print("\nOptions:")
            print("1. List courses")
            print("2. List students")
            print("3. Select a course and input marks")
            print("4. Show student marks for a course")
            print("5. Exit")
            print("6. Calculate and show GPA")
            print("7. Sort students by GPA")


            choice = input("Choose an option: ")
            if choice == "1":
                self.list_courses()
            elif choice == "2":
                self.list_students()
            elif choice == "3":
                course = self.select_course()
                self.input_marks(course)
            elif choice == "4":
                course = self.select_course()
                self.show_student_marks(course)
            elif choice == "6":
                self.calculate_gpa()
                for students in self._students:
                    print(f"{students.get_name()} (ID: {students.get_id()}), gpa: {self._gpa.get(students.get_id(), 0)}")
            elif choice == "7":
                self.sort_student_by_gpa()
            elif choice == "5":
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Try again.")


if __name__ == "__main__":
    smm = StudentMarkManagement()
    smm.run()
