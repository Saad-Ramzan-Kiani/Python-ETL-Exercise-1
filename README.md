# Python-ETL-Exercise-1
Python-ETL-Exercise 1

FUNCTIONAL PROGRAMMING
Exercise 1: Modularizing Python Code (Functional Programming)
Objective:
 Refactor a simple data processing script into modular, reusable functions using functional programming principles.
Task:
1.	Write a script that reads a CSV file (employees.csv), filters employees older than 30, calculates their salary after tax (10% deduction), and writes the processed data to a new CSV.

2.	Break down the script into functions (e.g., read_csv, filter_employees, calculate_tax, write_csv).

3.	Use lambda functions and map/filter/reduce where applicable.

________________________________________
Exercise 2: Create an ELT Pipeline (Ingest, Transform, Load)
Objective:
 Develop an end-to-end ELT pipeline that extracts data from an API, processes it in Python, and loads it into a database.
Task:
1.	Extract data from this API.

2.	Transform the data by extracting id, name, and email, and converting names to uppercase.

3.	Load the transformed data into a SQLite database.

Tools:
●	requests (for API calls)

●	pandas (for transformation)

●	sqlite3 (for loading into a database) Note: You need to import sqlite3. You can intall by “pip install sqlite3”

