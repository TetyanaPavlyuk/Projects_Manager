import csv
import sqlite3


connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()

with open("db_data/users.csv", "r") as users_file:
    content = csv.reader(users_file)
    next(content)
    insert_records = ("INSERT OR REPLACE INTO projects_user "
                      "(id, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, password) "
                      "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")

    cursor.executemany(insert_records, content)
    connection.commit()

with open("db_data/projects.csv", "r") as projects_file:
    content = csv.reader(projects_file)
    next(content)
    insert_records = ("INSERT OR REPLACE INTO projects_project "
                      "(id, name, owner_id, estimated_budget) "
                      "VALUES (?, ?, ?, ?)")
    cursor.executemany(insert_records, content)
    connection.commit()

with open("db_data/project_employees.csv", "r") as proj_emp_file:
    content = csv.reader(proj_emp_file)
    next(content)
    insert_records = ("INSERT OR REPLACE INTO projects_project_employees "
                      "(project_id, user_id) VALUES (?, ?)")
    cursor.executemany(insert_records, content)
    connection.commit()

with open("db_data/feedbacks.csv", "r") as feedbacks_file:
    content = csv.reader(feedbacks_file)
    next(content)
    insert_records = ("INSERT OR REPLACE INTO projects_feedback "
                      "(id, project_id, employee_id, rating, comment, created_at) "
                      "VALUES (?, ?, ?, ?, ?, ?)")
    cursor.executemany(insert_records, content)
    connection.commit()

connection.close()
