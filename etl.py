import csv
import sqlite3

print("--- Extracting Student Data ---")

with open("data/raw_student_performance.csv", "r") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

print(f"Total students: {len(rows)}")

print("\n--- Transforming Data ---")

valid_rows = []
invalid_rows = 0

for row in rows:
    try:
        marks = float(row["marks"])
        attendance = float(row["attendance"])

        if marks < 0 or marks > 100:
            invalid_rows += 1
            continue

        if attendance < 0 or attendance > 100:
            invalid_rows += 1
            continue

        row["marks"] = marks
        row["attendance"] = attendance
        valid_rows.append(row)

    except (ValueError, TypeError):
        invalid_rows += 1

print(f"Valid records: {len(valid_rows)}")
print(f"Invalid records skipped: {invalid_rows}")

print("\n--- Loading into SQLite ---")

conn = sqlite3.connect("student_performance.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS student_performance")

cursor.execute("""
CREATE TABLE student_performance (
    student_id TEXT,
    name TEXT,
    subject TEXT,
    marks REAL,
    attendance REAL
)
""")

for row in valid_rows:
    cursor.execute("""
    INSERT INTO student_performance
    VALUES (?, ?, ?, ?, ?)
    """, (
        row["student_id"],
        row["name"],
        row["subject"],
        row["marks"],
        row["attendance"]
    ))

conn.commit()

print(f"Loaded records: {len(valid_rows)}")

print("\n--- SQL Analysis ---")

cursor.execute("SELECT AVG(marks) FROM student_performance")
average_marks = cursor.fetchone()[0]

print(f"Average Marks: {average_marks:.2f}")

cursor.execute("""
SELECT subject, AVG(marks)
FROM student_performance
GROUP BY subject
ORDER BY AVG(marks) DESC
""")

print("\nAverage Marks by Subject:")

for subject, avg_marks in cursor.fetchall():
    print(f"{subject}: {avg_marks:.2f}")

conn.close()

print("\n--- ETL Pipeline Completed Successfully ---")
