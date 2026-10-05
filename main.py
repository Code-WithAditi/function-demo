import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_db"
)

cursor = conn.cursor()

# Insert Student
def add_student():
    name = input("Enter student name: ")
    course = input("Enter course: ")
    age = int(input("Enter age: "))

    query = """
    INSERT INTO students (name, course, age)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (name, course, age))
    conn.commit()

    print(" Student added successfully!")


# Display Students
def show_students():
    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print("\n--- Student Records ---")

    for student in students:
        print(student)


# Menu
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print(" Invalid choice!")

cursor.close()
conn.close()