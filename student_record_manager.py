# 1. Student Class
class Student:
    def __init__(self, student_id, name, course, year):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.year = year

    def display(self):
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Course     :", self.course)
        print("Year Level :", self.year)


# 2. Dynamic Array
class DynamicArray:
    def __init__(self):
        self.array = [None] * 5
        self.size_value = 0

    # 3. Add Student
    def add(self, student):
        if self.size_value == len(self.array):
            self.resize()

        self.array[self.size_value] = student
        self.size_value += 1

    # 4. Resize
    def resize(self):
        old = len(self.array)
        new = old * 2
        temp = [None] * new

        for i in range(self.size_value):
            temp[i] = self.array[i]

        self.array = temp

        print("Array is full.")
        print("Capacity increased from", old, "to", new)

    # 5. Get
    def get(self, index):
        if 0 <= index < self.size_value:
            return self.array[index]
        return None

    # 6. Set
    def set(self, index, student):
        if 0 <= index < self.size_value:
            self.array[index] = student
            return True
        return False

    # 7. Search
    def search(self, student_id):
        for i in range(self.size_value):
            if self.array[i].student_id.lower() == student_id.lower():
                return self.array[i]
        return None

    # 8. Find Index
    def search_index(self, student_id):
        for i in range(self.size_value):
            if self.array[i].student_id.lower() == student_id.lower():
                return i
        return -1

    # 9. Remove
    def remove(self, student_id):
        index = self.search_index(student_id)

        if index == -1:
            return False

        for i in range(index, self.size_value - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.size_value - 1] = None
        self.size_value -= 1
        return True

    # 10. Size and Capacity
    def size(self):
        return self.size_value

    def capacity(self):
        return len(self.array)

    # 11. Display Students
    def display(self):
        if self.size_value == 0:
            print("No student records available.")
            return

        print("\n===== STUDENT RECORDS =====")

        for i in range(self.size_value):
            print("\nStudent #", i + 1)
            self.array[i].display()


# 12. Input Validation
def read_text(message):
    while True:
        value = input(message).strip()

        if value != "":
            return value

        print("Input cannot be empty.")


def read_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number.")


def read_year():
    while True:
        year = read_int("Enter Year Level (1-6): ")

        if 1 <= year <= 6:
            return year

        print("Year level must be 1-6.")


# 13. Add Student Function
def add_student(records):
    print("\n===== ADD STUDENT =====")

    student_id = read_text("Enter Student ID: ")

    if records.search(student_id) is not None:
        print("Student ID already exists.")
        return

    name = read_text("Enter Student Name: ")
    course = read_text("Enter Course: ")
    year = read_year()

    records.add(Student(student_id, name, course, year))
    print("Student added successfully.")


# 14. Search Student
def search_student(records):
    student_id = read_text("Enter Student ID: ")
    student = records.search(student_id)

    if student is None:
        print("Student not found.")
    else:
        print("\nStudent found:")
        student.display()


# 15. Update Student
def update_student(records):
    student_id = read_text("Enter Student ID: ")
    index = records.search_index(student_id)

    if index == -1:
        print("Student not found.")
        return

    name = read_text("Enter new Student Name: ")
    course = read_text("Enter new Course: ")
    year = read_year()

    records.set(index, Student(student_id, name, course, year))
    print("Student updated successfully.")


# 16. Remove Student
def remove_student(records):
    student_id = read_text("Enter Student ID: ")

    if records.remove(student_id):
        print("Student removed successfully.")
    else:
        print("Student not found.")


# 17. Main Menu
def main():
    records = DynamicArray()

    while True:
        print("\n================================")
        print("     STUDENT RECORD MANAGER")
        print("================================")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Remove Student")
        print("6. Display Array Information")
        print("7. Exit")

        choice = read_int("Enter your choice: ")

        if choice == 1:
            add_student(records)

        elif choice == 2:
            records.display()

        elif choice == 3:
            search_student(records)

        elif choice == 4:
            update_student(records)

        elif choice == 5:
            remove_student(records)

        elif choice == 6:
            print("\nNumber of students:", records.size())
            print("Array capacity:", records.capacity())

        elif choice == 7:
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


# 18. Start Program
if __name__ == "__main__":
    main()
