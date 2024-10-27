import sqlite3

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE students (
                    student_id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER
                )''')
cursor.execute('''CREATE TABLE grades (
                    student_id INTEGER,
                    subject TEXT,
                    grade REAL
                )''')

cursor.executemany('INSERT INTO students (student_id, name, age) VALUES (?, ?, ?)', [
    (1, 'Alice', 19), (2, 'Bob', 22), (3, 'Charlie', 18), (4, 'Daisy', 21)
])

cursor.executemany('INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)', [
    (1, 'Math', 85), (1, 'Science', 90), (2, 'Math', 78), (2, 'Science', 82),
    (3, 'Math', 92), (3, 'Science', 88), (4, 'Math', 76), (4, 'Science', 85)
])


cursor.execute('''SELECT subject, AVG(grade) AS average_grade
           FROM grades
           JOIN students ON grades.student_id = students.student_id
           WHERE students.age < 20
           GROUP BY subject''')
results = cursor.fetchall()
for result in results:
    print(result)

connection.close()
