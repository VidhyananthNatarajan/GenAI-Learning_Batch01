import sqlite3
import os

# creating the directory

os.makedirs("db",exist_ok=True)

conn = sqlite3.connect("db/employee.db")
cursor = conn.cursor()

#create table

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
department TEXT NOT NULL,
salary INTEGER NOT NULL
) """)

# check if data already exists
cursor.execute("SELECT COUNT(*) FROM employees")
count = cursor.fetchone()[0]

if count ==0:
    employees =[
        ("User01","HR",65000),
        ("User02","IT",125000),
        ("User03","Finance",165000),
        ("User04","IT",135000),
        ("User05","HR",95000), 
    ]

    cursor.executemany(
      "INSERT INTO employees(name,department,salary) VALUES(?,?,?)",employees)

    print("Data inserted successfully")

else:

    print("Datatbase already contains data.")

conn.commit()
conn.close()

print("Database Intialized")