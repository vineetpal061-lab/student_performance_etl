# Student Performance Data Pipeline

A beginner-friendly Data Engineering project that processes student performance data using Python, CSV, SQLite, and SQL.

## ETL Flow
CSV → Extract → Validate → Transform → SQLite → SQL Analysis

## Tech Stack

- Python
- CSV
- SQLite
- SQL
- Git & GitHub

## What the Pipeline Does

1. Reads raw student performance data from CSV
2. Validates marks and attendance values
3. Converts marks and attendance to numeric values
4. Skips invalid records
5. Loads cleaned data into SQLite
6. Calculates overall average marks using SQL
7. Calculates average marks by subject using SQL

## Sample Results

- Total students: 8
- Valid records: 8
- Invalid records skipped: 0
- Overall average marks: 78.00
- Python average marks: 74.00
- SQL average marks: 82.00

## Project Structure

```text
student_performance_etl/
├── data/
│   └── raw_student_performance.csv
├── etl.py
├── README.md
└── .gitignore
