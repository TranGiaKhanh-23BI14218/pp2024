# 1.student.mark.py

def input_number_of_students():
    return int(input("Enter the number of students: "))

def input_student_information():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
    return (student_id, name, dob)

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_information():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return (course_id, name)

def select_course(courses):
    print("\nAvailable courses:")
    for idx, course in enumerate(courses, 1):
        print(f"{idx}. {course[1]} (ID: {course[0]})")
    selected_index = int(input("Select a course by number: ")) - 1
    return courses[selected_index]

def input_marks_for_course(course, students, marks):
    print(f"\nEntering marks for course: {course[1]} (ID: {course[0]})")
    for student in students:
        mark = float(input(f"Enter marks for {student[1]} (ID: {student[0]}): "))
        marks[(student[0], course[0])] = mark

def list_courses(courses):
    print("\nList of courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def list_students(students):
    print("\nList of students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

def show_student_marks(course, students, marks):
    print(f"\nMarks for course: {course[1]} (ID: {course[0]})")
    for student in students:
        key = (student[0], course[0])
        mark = marks.get(key, "N/A")
        print(f"{student[1]} (ID: {student[0]}): {mark}")

def main():
    print("Student Mark Management System")

    # Input data
    students = []
    courses = []
    marks = {}

    num_students = input_number_of_students()
    for _ in range(num_students):
        students.append(input_student_information())

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        courses.append(input_course_information())

    # Menu loop
    while True:
        print("\nOptions:")
        print("1. List courses")
        print("2. List students")
        print("3. Select a course and input marks")
        print("4. Show student marks for a course")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            list_courses(courses)
        elif choice == "2":
            list_students(students)
        elif choice == "3":
            course = select_course(courses)
            input_marks_for_course(course, students, marks)
        elif choice == "4":
            course = select_course(courses)
            show_student_marks(course, students, marks)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
