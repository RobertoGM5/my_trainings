import sqlite3

database_path = 'test.db'

# Connecting to the SQLite database (if it doesn't exist, it will be created)
connection = sqlite3.connect(database_path)

# Creating a cursor object to interact with the database
cursor = connection.cursor()

# Creating a table for students
create_table = '''
CREATE TABLE IF NOT EXISTS students(
student_id INTEGER PRIMARY KEY NOT NULL,
student_name TEXT NOT NULL
);
'''

# Executing the query to create the table
cursor.execute(create_table)

# Committing the changes
connection.commit()

# Inserting values into the students table
insert_query = '''
INSERT INTO students
(student_id, student_name)
VALUES
(1,'John Doe'),
(2, 'Sita Murray'),
(3, 'Earl Gray');
'''

# Executing the insert query
cursor.execute(insert_query)

# Committing the changes
connection.commit()

# Reading all records from the students table
select_query = "SELECT * FROM students;"

# Executing the select query
cursor.execute(select_query)

# Fetching all rows
rows = cursor.fetchall()

# Displaying the results
print('Contents of the students table:')

for row in rows:
    print(row)

# Closing the connection
connection.close()